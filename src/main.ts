import { World, Game } from './world';
import type { Character, CharacterData } from './types';
import './style.css';

let world: World;
let game: Game | null = null;

const app = document.querySelector<HTMLDivElement>('#app')!;

async function init() {
  const res = await fetch('../character.json');
  console.log("this is not the problem")
  const data: CharacterData[] = await res.json();
  world = new World(data);
  render();

}

function render() {
  if (!world) return;
  if (!game) {
    renderMenu();
  } else {
    renderGame();
  }
}

function renderMenu() {
  app.innerHTML = `
    <div class="menu">
      <h1>Collable</h1>
      <p class="subtitle">Connect two characters through shared groups</p>
      
      <div class="menu-buttons">
        <button id="random-game" class="btn btn-primary">Random Game</button>
        <button id="custom-game" class="btn btn-secondary">Custom Game</button>
        <button id="daily-game" class="btn btn-accent">Daily Game</button>
      </div>

      <div id="custom-game-setup" class="custom-setup hidden">
        <h2>Custom Game</h2>
        <div class="character-select">
          <div class="select-group">
            <label>Start Character:</label>
            <input type="text" id="start-search" placeholder="Search character..." />
            <div id="start-results" class="search-results"></div>
            <div id="start-selected" class="selected-character">None</div>
          </div>
          <div class="select-group">
            <label>End Character:</label>
            <input type="text" id="end-search" placeholder="Search character..." />
            <div id="end-results" class="search-results"></div>
            <div id="end-selected" class="selected-character">None</div>
          </div>
        </div>
        <button id="start-custom" class="btn btn-primary" disabled>Start Game</button>
      </div>

      <div class="stats">
        <p>${world.characters.length} characters</p>
        <p>${world.groups.length} groups</p>
      </div>
    </div>
  `;

  document.getElementById('random-game')!.onclick = () => {
    const { start, end } = world.createRandomGame();
    game = new Game(world, start, end, render);
    render();
  };

  document.getElementById('daily-game')!.onclick = () => {
    const today = new Date();
    let seed = Math.floor(today.getTime() / (1000 * 60 * 60 * 24));
    
    const random = (s: number) => {
      let x = Math.sin(s) * 10000;
      return x - Math.floor(x);
    };

    let start = world.characters[Math.floor(random(seed) * world.characters.length)];
    let end = world.characters[Math.floor(random(seed + 1) * world.characters.length)];
    while (start === end || start.groups.some(g => end.groups.includes(g))) {
      seed ++;
      end = world.characters[Math.floor(random(seed + 1) * world.characters.length)];
    }

    game = new Game(world, start, end, render);
    render();
  };

  document.getElementById('custom-game')!.onclick = () => {
    document.getElementById('custom-game-setup')!.classList.toggle('hidden');
  };

  let selectedStart: Character | null = null;
  let selectedEnd: Character | null = null;

  const setupSearch = (type: 'start' | 'end') => {
    const searchInput = document.getElementById(`${type}-search`) as HTMLInputElement;
    const resultsDiv = document.getElementById(`${type}-results`)!;
    const selectedDiv = document.getElementById(`${type}-selected`)!;

    searchInput.oninput = () => {
      const query = searchInput.value;
      const results = world.searchCharacters(query).slice(0, 20);
      
      resultsDiv.innerHTML = results.map(c => 
        `<div class="search-item" data-name="${c.name}" data-origin="${c.origin}">
          ${c.name} <span class="origin">(${c.origin})</span>
        </div>`
      ).join('');

      resultsDiv.querySelectorAll('.search-item').forEach((item: Element) => {
        (item as HTMLElement).onclick = () => {
          const name = item.getAttribute('data-name')!;
          const origin = item.getAttribute('data-origin')!;
          const character = world.characters.find(c => c.name === name && c.origin === origin)!;
          
          if (type === 'start') {
            selectedStart = character;
            selectedDiv.innerHTML = `${character.name} <span class="origin">(${character.origin})</span>`;
          } else {
            selectedEnd = character;
            selectedDiv.innerHTML = `${character.name} <span class="origin">(${character.origin})</span>`;
          }

          resultsDiv.innerHTML = '';
          searchInput.value = '';

          const startBtn = document.getElementById('start-custom') as HTMLButtonElement;
          startBtn.disabled = !selectedStart || !selectedEnd;
        };
      });
    };
  };

  setupSearch('start');
  setupSearch('end');

  document.getElementById('start-custom')!.onclick = () => {
    if (selectedStart && selectedEnd) {
      game = new Game(world, selectedStart, selectedEnd, render);
      render();
    }
  };
}

function renderGame() {
  if (!game) return;

  const { state } = game;
  const groups = game.getCurrentCharacterGroups();

  app.innerHTML = `
    <div class="game">
      <div class="game-header">
        <button id="back-btn" class="btn btn-small" ${state.history.length === 0 ? 'disabled' : ''}>← Back</button>
        <div class="round">Round: ${state.round}</div>
        <button id="menu-btn" class="btn btn-small">Menu</button>
      </div>

      <div class="game-info">
        <div class="character-card start">
          <span class="label">Start</span>
          <span class="name">${state.start.name}</span>
          <span class="origin">${state.start.origin}</span>
        </div>
        <div class="arrow">→</div>
        <div class="character-card current">
          <span class="label">Current</span>
          <span class="name">${state.current.name}</span>
          <span class="origin">${state.current.origin}</span>
        </div>
        <div class="arrow">→</div>
        <div class="character-card end">
          <span class="label">End</span>
          <span class="name">${state.end.name}</span>
          <span class="origin">${state.end.origin}</span>
        </div>
      </div>

      ${state.phase === 'won' ? `
        <div class="win-message">
          <h2>You Won!</h2>
          <p>Completed in ${state.round} rounds</p>
          <button id="play-again" class="btn btn-primary">Play Again</button>
        </div>
      ` : `
        <div class="game-content">
          ${state.phase === 'select_group' ? `
            <h2>Select a group</h2>
            <div class="group-list">
              ${groups.map(g => `
                <button class="group-btn" data-group="${g.name}">
                  ${g.name}
                  <span class="count">(${g.characters.length})</span>
                </button>
              `).join('')}
            </div>
          ` : `
            <h2>Select a character from ${state.selectedGroup?.name}</h2>
            <div class="character-list">
              ${game.getGroupCharacters().map(c => `
                <button class="character-btn" data-name="${c.name}" data-origin="${c.origin}">
                  ${c.name}
                  <span class="origin">${c.origin}</span>
                </button>
              `).join('')}
            </div>
          `}
        </div>
      `}

      <div class="history">
        <h3>Path</h3>
        <div class="history-path">
          ${state.history.map((h, i) => `
            <div class="history-step">
              <span class="character">${h.character.name}</span>
              <span class="group">via ${h.group.name}</span>
              ${i < state.history.length - 1 ? '<span class="arrow">→</span>' : ''}
            </div>
          `).join('')}
          ${state.history.length > 0 ? '<span class="arrow">→</span>' : ''}
          <span class="character current">${state.current.name}</span>
        </div>
      </div>
    </div>
  `;

  document.getElementById('back-btn')!.onclick = () => game?.goBack();
  document.getElementById('menu-btn')!.onclick = () => {
    game = null;
    render();
  };

  document.querySelectorAll('.group-btn').forEach((btn: Element) => {
    (btn as HTMLElement).onclick = () => {
      const groupName = btn.getAttribute('data-group')!;
      const group = groups.find(g => g.name === groupName)!;
      game?.selectGroup(group);
    };
  });

  document.querySelectorAll('.character-btn').forEach((btn: Element) => {
    (btn as HTMLElement).onclick = () => {
      const name = btn.getAttribute('data-name')!;
      const origin = btn.getAttribute('data-origin')!;
      const characters = game?.getGroupCharacters() || [];
      const character = characters.find(c => c.name === name && c.origin === origin)!;
      game?.selectCharacter(character);
    };
  });

  const playAgainBtn = document.getElementById('play-again');
  if (playAgainBtn) {
    playAgainBtn.onclick = () => {
      const { start, end } = world.createRandomGame();
      game = new Game(world, start, end, render);
      render();
    };
  }
}

init();
