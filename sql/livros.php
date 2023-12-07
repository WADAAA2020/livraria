<?php

echo "<h2>Livros</h2>";

function InserirLivros($nome, $ano){

    //livraria é o nome do meu bd
    $conexao = new PDO("mysql:host=localhost;dbname=livraria", "root", "");

    $insertLivros = "INSERT INTO tb_livros (nome, autor, editora, genero) VALUES (:nome, :autor, :editora, :genero)";

    //$nome = 'HP'
    //$ano = '2015'

    $preparacao = $conexao->prepare($insertLivros);

    $preparacao->bindParam(":nome", $nome);
    $preparacao->bindParam(":autor", $autor);
    $preparacao->bindParam(":editora", $editora);
    $preparacao->bindParam(":genero", $genero);

    $preparacao->execute();
}

InserirLivros("Lol", "Rito", "EUA", "Ação");

?>