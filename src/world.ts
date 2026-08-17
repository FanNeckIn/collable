import type { Character, CharacterData, Group, GamePhase } from './types';

export class World {
  groups: Group[] = [];
  characters: Character[] = [];

  constructor(data: CharacterData[]) {
    this.addCharacters(data);
  }

  private addCharacters(data: CharacterData[]): void {
    for (const item of data) {
      const char: Character = {
        name: item.name,
        origin: item.origin,
        groups: item.groups
      };
      this.characters.push(char);

      for (const groupName of item.groups) {
        let group = this.groups.find(g => g.name === groupName);
        if (!group) {
          group = { name: groupName, characters: [] };
          this.groups.push(group);
        }
        group.characters.push(char);
      }
    }
  }

  getCharacterGroups(character: Character): Group[] {
    return this.groups.filter(g => character.groups.includes(g.name));
  }

  searchCharacters(query: string): Character[] {
    if (!query) return [];
    const lower = query.toLowerCase();
    return this.characters.filter(c => 
      c.name.toLowerCase().includes(lower) ||
      c.origin.toLowerCase().includes(lower)
    );
  }

  searchGroups(query: string): Group[] {
    if (!query) return [];
    const lower = query.toLowerCase();
    return this.groups.filter(g => 
      g.name.toLowerCase().includes(lower)
    );
  }

  getRandomCharacter(): Character {
    return this.characters[Math.floor(Math.random() * this.characters.length)];
  }

  createRandomGame(): { start: Character; end: Character } {
    let start = this.getRandomCharacter();
    let end = this.getRandomCharacter();
    while (start === end) {
      end = this.getRandomCharacter();
    }
    return { start, end };
  }
}

export interface GameState {
  start: Character;
  end: Character;
  current: Character;
  round: number;
  phase: GamePhase;
  selectedGroup: Group | null;
  history: { character: Character; group: Group }[];
}

export class Game {
  private world: World;
  state: GameState;
  private onStateChange: () => void;

  constructor(world: World, start: Character, end: Character, onStateChange: () => void) {
    this.world = world;
    this.onStateChange = onStateChange;
    this.state = {
      start,
      end,
      current: start,
      round: 0,
      phase: 'select_group',
      selectedGroup: null,
      history: []
    };
  }

  getCurrentCharacterGroups(): Group[] {
    return this.world.getCharacterGroups(this.state.current);
  }

  getGroupCharacters(): Character[] {
    return this.state.selectedGroup?.characters || [];
  }

  selectGroup(group: Group): void {
    if (this.state.phase !== 'select_group') return;
    this.state.selectedGroup = group;
    this.state.phase = 'select_character';
    this.onStateChange();
  }

  selectCharacter(character: Character): void {
    if (this.state.phase !== 'select_character') return;
    if (!this.state.selectedGroup) return;

    this.state.history.push({
      character: this.state.current,
      group: this.state.selectedGroup
    });

    this.state.current = character;
    this.state.round++;
    this.state.selectedGroup = null;

    if (this.state.current === this.state.end) {
      this.state.phase = 'won';
    } else {
      this.state.phase = 'select_group';
    }

    this.onStateChange();
  }

  goBack(): void {
    if (this.state.history.length === 0) return;

    const last = this.state.history.pop()!;
    this.state.current = last.character;
    this.state.round--;
    this.state.selectedGroup = null;
    this.state.phase = 'select_group';
    this.onStateChange();
  }

  reset(): void {
    this.state = {
      start: this.state.start,
      end: this.state.end,
      current: this.state.start,
      round: 0,
      phase: 'select_group',
      selectedGroup: null,
      history: []
    };
    this.onStateChange();
  }
}
