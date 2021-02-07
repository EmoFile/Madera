console.log("testA")
$(() => {
  let $navDiv = document.getElementById('navigation')
  console.log($navDiv)
  console.log("test")
  let $ul = document.createElement('ul')
  console.log($ul)

  let $li = document.createElement('li')
  let $button = document.createElement('button')
  $button.setAttribute('id',
    `creation-devis`)
  $ul.setAttribute('id', 'nav-bar')
  $button.innerText = 'Creation devis'

  $li.append($button)
  $ul.append($li)
  $navDiv.append($ul)

  $('#creation-devis').click(function () {
    let devisJSON = {
      "nom": $inputNomDevis.value,
      "commercial": 1,
      "client": 1,
      "pieces": [],
    }
    let $mainDiv = document.getElementById('main-content')
    let $devisForm = document.createElement('form')
    $devisForm.setAttribute('id', 'devis-form')

    let $devisDiv = document.createElement('div')
    $devisDiv.setAttribute('id', 'devis-div')

    //region top-devis
    let $topDevisDiv = document.createElement('div')
    $topDevisDiv.setAttribute('id', 'top-devis-div')
    let $labelNomDevis = document.createElement('label')
    $labelNomDevis.setAttribute('for', 'nom')
    $labelNomDevis.innerText = "Nom du devis : "
    let $inputNomDevis = document.createElement('input')
    $inputNomDevis.setAttribute('id', 'nom')
    $inputNomDevis.setAttribute('name', 'nom')
    $inputNomDevis.setAttribute('type', 'text')

    $topDevisDiv.append($labelNomDevis)
    $topDevisDiv.append($inputNomDevis)
    //endregion

    //region center-devis
    let $centerDevisDiv = document.createElement('div')
    let $centerLeftDevisDiv = document.createElement('div')
    let $centerRightDevisDiv = document.createElement('div')
    $centerLeftDevisDiv.setAttribute('id', 'center-left-devis-div')
    $centerRightDevisDiv.setAttribute('id', 'center-right-devis-div')
    $centerDevisDiv.setAttribute('id', 'center-devis-div')
    let $pAjtPiece = document.createElement('p')
    $pAjtPiece.innerText = 'Ajouter une pièce'
    let $buttonAjtPiece = document.createElement('button')
    $buttonAjtPiece.setAttribute('type',
      `button`)
    $buttonAjtPiece.setAttribute('id',
      `ajouter-piece`)
    $buttonAjtPiece.innerText = "+"
    $centerLeftDevisDiv.append($pAjtPiece)
    $centerLeftDevisDiv.append($buttonAjtPiece)
    $centerDevisDiv.append($centerLeftDevisDiv)
    $centerDevisDiv.append($centerRightDevisDiv)
    //endregion

    //region bottom-devis
    let $bottomDevisDiv = document.createElement('div')
    $bottomDevisDiv.setAttribute('id', 'bottom-devis-div')
    let $pPriceDevis = document.createElement('p')
    $pPriceDevis.setAttribute('id', 'price-devis')
    $pPriceDevis.innerText = "0"
    let $pTextPriceDevis = document.createElement('p')
    $pTextPriceDevis.innerText = "Prix :"
    $bottomDevisDiv.append($pTextPriceDevis)
    $bottomDevisDiv.append($pPriceDevis)
    //endregion


    $devisDiv.append($topDevisDiv)
    $devisDiv.append($centerDevisDiv)
    $devisDiv.append($bottomDevisDiv)
    $devisForm.append($devisDiv)
    $mainDiv.append($devisForm)

    $('#ajouter-piece').click(function () {
      let devisJSON = {
        "nom": $inputNomDevis.value,
        "commercial": 1,
        "client": 1,
        "pieces": [],
      }
      console.log(devisJSON)
    });
  });
});
