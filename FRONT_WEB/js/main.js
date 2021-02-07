var $gammes = [{"id_gamme": 1, "nom": "Portes"}, {"id_gamme": 2, "nom": "Murs"}]
var $modules = [{"id_gamme": 1, "id_module": 1, "nom": "Porte en bois"},
    {"id_gamme": 1, "id_module": 2, "nom": "Porte en PVC"},
    {"id_gamme": 2, "id_module": 3, "nom": "Mur 4x2"},
    {"id_gamme": 2, "id_module": 4, "nom": "Mur 5x2"}]
var devisJSON = {
    "nom": "",
    "commercial": 1,
    "client": 1,
    "pieces": [],
}

const DELETEPIECE = {
    bind() {
        $(".delete-piece").attr('class', 'delete-piece btn btn-danger').click(function () {
            console.log($(this))

            let elem = document.getElementById($(this).attr('id'))
            console.log('elem:' + elem)

            let lio = elem.id.lastIndexOf('-');
            let idPiece = elem.id.slice(lio + 1);

            for (let i = 0; i < devisJSON.pieces.length; i++) {
                if (devisJSON["pieces"][i].id_front === parseInt(idPiece)) {
                    devisJSON.pieces.splice(i, 1);
                    elem.parentElement.remove()
                }
            }
            console.log(devisJSON)
        });
    }
};

$(() => {

    let $navDiv = document.getElementById('navigation')
    let $ul = document.createElement('ul')


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
        document.getElementById('main-content').innerHTML = ""

        let $mainDiv = document.getElementById('main-content')
        $mainDiv.setAttribute('class', 'container-fluid')
        let $devisForm = document.createElement('form')
        $devisForm.setAttribute('id', 'devis-form')
        $devisForm.setAttribute('class', 'container-fluid')

        let $devisDiv = document.createElement('div')
        $devisDiv.setAttribute('id', 'devis-div')
        $devisDiv.setAttribute('class', 'container-fluid')

        //region top-devis
        let $topDevisDiv = document.createElement('div')
        $topDevisDiv.setAttribute('id', 'top-devis-div')
        $topDevisDiv.setAttribute('class', 'row')
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
        $centerDevisDiv.setAttribute('class', 'row')
        let $centerLeftDevisDiv = document.createElement('div')
        let $centerRightDevisDiv = document.createElement('div')
        $centerLeftDevisDiv.setAttribute('id', 'center-left-devis-div')
        $centerLeftDevisDiv.setAttribute('class', 'col border')
        $centerRightDevisDiv.setAttribute('id', 'center-right-devis-div')
        $centerRightDevisDiv.setAttribute('class', 'col border')
        $centerDevisDiv.setAttribute('id', 'center-devis-div')
        $centerDevisDiv.setAttribute('class', 'row')

        let $buttonAjtPiece = document.createElement('button')
        $buttonAjtPiece.setAttribute('type', `button`)
        $buttonAjtPiece.setAttribute('id', `ajouter-piece`)
        $buttonAjtPiece.innerText = "Ajouter une pièce"
        $centerLeftDevisDiv.append($buttonAjtPiece)
        $centerDevisDiv.append($centerLeftDevisDiv)
        $centerDevisDiv.append($centerRightDevisDiv)
        //endregion

        //region bottom-devis
        let $bottomDevisDiv = document.createElement('div')
        $bottomDevisDiv.setAttribute('id', 'bottom-devis-div')
        $bottomDevisDiv.setAttribute('class', 'row')
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
            document.getElementById('center-right-devis-div').innerHTML = ""

            let $pieceDiv = document.createElement('div')
            $pieceDiv.setAttribute('id', 'piece-div')
            $pieceDiv.setAttribute('class', 'container-fluid border-1')
            let $topPieceDiv = document.createElement('div')
            $topPieceDiv.setAttribute('class', 'row')
            $topPieceDiv.setAttribute('id', 'top-piece-div')

            let $centerPieceDiv = document.createElement('div')
            $centerPieceDiv.setAttribute('class', 'container-fluid')
            $centerPieceDiv.setAttribute('id', 'center-piece-div')

            let $bottomPieceDiv = document.createElement('div')
            $bottomPieceDiv.setAttribute('class', 'row')
            $bottomPieceDiv.setAttribute('id', 'bottom-piece-div')

            let $pieceName = document.createElement('input')
            $pieceName.setAttribute('id', 'piece-name')
            $pieceName.setAttribute('type', 'text')
            $pieceName.setAttribute('name', 'piece-name')
            let $pieceNameLabel = document.createElement('label')
            $pieceNameLabel.setAttribute('for', 'piece-name')
            $pieceNameLabel.innerText = "Nom de la pièce"
            $topPieceDiv.append($pieceNameLabel)
            $topPieceDiv.append($pieceName)
            $pieceDiv.append($topPieceDiv)

            let $buttonValiderPiece = document.createElement('button')
            $buttonValiderPiece.setAttribute('type', `button`)
            $buttonValiderPiece.setAttribute('id', `valider-piece`)
            $buttonValiderPiece.innerText = "Valider"

            let $buttonAjouterModule = document.createElement('button')
            $buttonAjouterModule.setAttribute('type', `button`)
            $buttonAjouterModule.setAttribute('id', `ajouter-module`)
            $buttonAjouterModule.innerText = "Ajouter un module"

            $topPieceDiv.append($buttonAjouterModule)
            $bottomPieceDiv.append($buttonValiderPiece)
            $pieceDiv.append($centerPieceDiv)
            $pieceDiv.append($bottomPieceDiv)
            $centerRightDevisDiv.append($pieceDiv)

            $('#ajouter-module').click(function () {
                let $selectModuleDiv = document.createElement('div')
                $selectModuleDiv.setAttribute('class',
                    'row')
                let $selectModule = document.createElement('select')
                $selectModule.setAttribute('id',
                    'select-module-' + (document.getElementById('center-piece-div').childElementCount + 1))

                for (let i = 0; i < $gammes.length; i++) {
                    let $optGroup = document.createElement('optgroup')
                    $optGroup.setAttribute('label', $gammes[i].nom)
                    for (let j = 0; j < $modules.length; j++) {
                        if ($modules[j].id_gamme === $gammes[i].id_gamme) {
                            let $option = document.createElement('option')
                            $option.setAttribute('value', $modules[j].id_module)
                            $option.setAttribute('class', 'option-module')

                            $option.innerText = $modules[j].nom
                            $optGroup.append($option)
                        }
                    }
                    $selectModule.append($optGroup)
                    $selectModuleDiv.append($selectModule)
                    $centerPieceDiv.append($selectModuleDiv)
                }
            });
            $('#valider-piece').click(function () {
                devisJSON["nom"] = document.getElementById('nom').value
                devisJSON["commercial"] = 1
                devisJSON["client"] = 1
                let piece = {
                    "nom": document.getElementById('piece-name').value,
                    "id_front": devisJSON["pieces"].length + 1,
                    "modules": []
                }
                for (i = 1; i < document.getElementById('center-piece-div').childElementCount + 1; i++) {

                    var elem = document.getElementById('select-module-' + i)
                    let module = {"id_module": elem.value}
                    piece["modules"].push(module)
                }
                devisJSON["pieces"].push(piece)

                let $recapPieceDiv = document.createElement('div')
                $recapPieceDiv.setAttribute('id', `recap-piece-` + (devisJSON['pieces'].length))
                $recapPieceDiv.setAttribute('class', `row`)
                let $recapPieceNom = document.createElement('p')
                $recapPieceNom.setAttribute('class', `col`)
                $recapPieceNom.innerText = document.getElementById('piece-name').value
                let $deleteBtnRecapPiece = document.createElement('button')
                $deleteBtnRecapPiece.setAttribute('class', `col btn btn-danger delete-piece`)
                $deleteBtnRecapPiece.setAttribute('type', `button`)
                $deleteBtnRecapPiece.setAttribute('id', 'delete-recap-piece-' + (devisJSON['pieces'].length))
                $deleteBtnRecapPiece.innerText = 'X'
                $recapPieceDiv.append($recapPieceNom)
                $recapPieceDiv.append($deleteBtnRecapPiece)
                $centerLeftDevisDiv.append($recapPieceDiv)
                DELETEPIECE.bind()
                document.getElementById('center-right-devis-div').innerHTML = ""
                console.log(devisJSON)
            });
        });
    });
});
