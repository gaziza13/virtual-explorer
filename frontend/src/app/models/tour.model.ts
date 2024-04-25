export interface Tour{
    id: number;
    city: string;
    name: string;
    description: string;
    price: number;
    duration: string;
    categories: string[];
    imageLink: string;
    reviews?: number;
}
