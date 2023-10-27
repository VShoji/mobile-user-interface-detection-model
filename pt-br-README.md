# Detecção de Elementos de Interface de Usuário para mobile utilizando YOLOv7 para o Projeto Apprender

<p>Este repositório contém os pesos de um modelo pré-treinado e um script que converte as imagens do dataset RICO a um formato compatível com o YOLOv7.</p>

[Link do dataset](https://interactionmining.org/rico)</br>
[Link do YOLOv7](https://github.com/WongKinYiu/yolov7)

## Por que o Projeto Apprender é importante?

[O Projeto Apprender](https://github.com/VShoji/apprender-research "Apprender: Pesquisa") tem como objetivo ajudar as pessoas com dificuldades no processo de aprendizagem de novas tecnologias, como idosos e indivíduos que possuem pouca experiência com dispositivos eletrônicos, a utilizarem aparelhos celulares. </br>

Para pedir ajuda, o usuário escreve a tarefa que pretendem completar, como fazer login, postar uma foto ou adicionar um novo número de celular, após o qual o aplicativo automaticamente identifica que tipo de página o usuário está (como dashboards, páginas de login, posts e páginas de perfil) e fornece instruções de como completar a tarefa.</br>

Este repositório contém os pesos de um modelo pré-treinado de YOLOv7 que identifica multiplos tipos de elementos de interface de usuário em dispositivos mobile.</br>
Os tipos de elementos incluem:
- Advertisement
- Background Image
- Bottom Navigation
- Button Bar
- Card
- Checkbox
- Date Picker
- Drawer
- Icon
- Input
- List Item
- Map View
- Modal
- Multi-Tab
- Number Stepper
- On/Off Switch
- Pager Indicator
- Radio Button
- Text
- Text Button
- Video

## Como começar o treinamento
- Baixe os arquivos "UI Screenshots and View Hierarchies" e "UI Screenshots and Hierarchies with Semantic Annotations" deste link: https://interactionmining.org/rico
- Descompacte os arquivos
- Clone o [YOLOv7](https://github.com/WongKinYiu/yolov7)
- Monte a pasta da seguinte forma:
```
.
├───combined
├───dataset
│   ├───test
│   │   ├───images
│   │   └───labels
│   ├───train
│   │   ├───images
│   │   └───labels
│   └───valid
│       ├───images
│       └───labels
├───semantic_annotations
└───yolov7
```
- Instale as dependências com:
```
pip install -r requirements.txt
```
- Execute o script para converter o dataset para um formato compatível com o YOLOv7
```
python convert.py
```
- Siga as instruções do YOLOv7 para começar o treinamento
