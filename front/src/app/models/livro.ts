import { Autor } from "./autor";
import { Editora } from "./editora";

export interface Livro {
    id: number;
    titulo: string;
    subtitulo?: string | null;
    autor?: Autor | null;
    editora?: Editora | null;
    isbn?: string | null;
    descricao?: string | null;
    idioma?: string | null;
    ano_publicacao?: string | null;
    paginas?: number | null;
    preco?: number | null;
    estoque?: number | null;
    desconto?: number | null;
    disponivel?: number | null;
    dimensoes?: number | null;
    peso?: number | null;
}
