interface Animal {
    id: number,
    name: string,
    species: string,
    sex: string,
    birthday: string,
    weight: string,
    created: string
  }


  interface Animals {
    [key: string]: Animal
  }

  export type { Animal, Animals }