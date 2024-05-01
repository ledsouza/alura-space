# Aplicação Web de Galeria de Fotos do Espaço

Aplicação web de uma galeria de fotos desenvolvida utilizando django

| :books: Vitrine.Dev |     |
| -------------  | --- |
| :sparkles: Nome        | **Aplicação Web de Galeria de Fotos do Espaço**
| :label: Tecnologias | python, django, html, css, javascript, s3

## Galeria de Fotos

A aplicação permite a visualização de um catálogo de fotos, contendo informações detalhadas sobre cada uma das fotos individuais. As fotografia estão categorizadas, permitindo filtros personalizados por tags. Caso haja interesse de buscar fotos específicas, um campo de busca é disponibilizado para o usuário.

## Autenticação de Usuários

Apenas usuários autenticados são permitidos o acesso a galeria de fotos. Caso não seja autenticado, haverá uma página dedicada ao cadastro do usuário para obter o acesso completo da galeria.

## Adição, Edição e Remoção

É permitido aos usuários inserir, editar e remover as fotografias da galera. Porém, apenas usuários com permissões de admin poderão decidir quais fotografias estarão publicadas na galeria. Os grupos de usuários são definidos a partir da página de admin, havendo acesso apenas para os usuários que são definidos como admin.
