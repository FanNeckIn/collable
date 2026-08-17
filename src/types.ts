export interface CharacterData {
  name: string;
  origin: string;
  groups: string[];
}

export interface Character {
  name: string;
  origin: string;
  groups: string[];
}

export interface Group {
  name: string;
  characters: Character[];
}

export type GamePhase = 'select_group' | 'select_character' | 'won';
