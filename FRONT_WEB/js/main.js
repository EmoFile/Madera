var $products = null
var $devis = null

$.ajax({
    url: 'http://127.0.0.1:8000/products/',
    type: 'get',
    contentType: 'application/json',
}).done(function (msg, status, jqXHR) {
    /*    console.log(msg)
        console.log(status)
        console.log(jqXHR)*/
    $products = msg["products"]
    console.log($products)

})
var $clients = [{"id_erp": 1, "id_client": 1, "mail": "richard.sivera@free.fr"},
    {"id_erp": 2, "id_client": 2, "mail": "marine.legast@free.fr"},]
var $commercial = [{"id_erp": 1, "id_client": 1, "mail": "richard.sivera@free.fr"},
    {"id_erp": 2, "id_client": 2, "mail": "marine.legast@free.fr"},]
var devisJSON = {
    "prix": 0,
    "nom_devis": "",
    "commercial": null,
    "client": null,
    "plan": null,
    "pieces": [],
}

const DELETEPIECE = {
    bind() {
        $(".delete-piece").attr('class', 'delete-piece btn btn-danger').click(function () {
            //console.log($(this))

            let elem = document.getElementById($(this).attr('id'))
            //console.log(elem)

            let lio = elem.id.lastIndexOf('-');
            let idPiece = elem.id.slice(lio + 1);
            let $prixToRemove = document.getElementById('prix-recap-piece-' + idPiece)
            $prixToRemove = parseInt($prixToRemove.innerText)
            let $prixToUpdate = document.getElementById('price-devis')
            $prixToUpdate.innerText = parseInt($prixToUpdate.innerText) - $prixToRemove
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
    //region CONSTRUCTION-NAVBAR
    let $navDiv = document.getElementById('navigation')
    $navDiv.setAttribute('id', 'nav-bar')

    let $buttonCreationDevis = document.createElement('button')
    $buttonCreationDevis.setAttribute('id',
        `creation-devis`)
    $buttonCreationDevis.setAttribute('class',
        `m-1`)
    $buttonCreationDevis.innerText = 'Creation devis'

    let $buttonCreationCompte = document.createElement('button')
    $buttonCreationCompte.setAttribute('id',
        `creation-compte`)
    $buttonCreationCompte.setAttribute('class',
        `m-1`)
    $buttonCreationCompte.innerText = 'Creation compte'


    let $buttonCreationCompteInterne = document.createElement('button')
    $buttonCreationCompteInterne.setAttribute('id',
        `creation-compte-interne`)
    $buttonCreationCompteInterne.setAttribute('class',
        `m-1`)
    $buttonCreationCompteInterne.innerText = 'Creation compte interne'

    let $buttonVueBI = document.createElement('button')
    $buttonVueBI.setAttribute('id',
        `vue-bi`)
    $buttonVueBI.setAttribute('class',
        `m-1`)
    $buttonVueBI.innerText = 'Vue BI'

    let $buttonHome = document.createElement('button')
    $buttonHome.setAttribute('id',
        `home`)
    $buttonHome.setAttribute('class',
        `m-1`)
    $buttonHome.innerText = 'Home'

    let $buttonRendezVous = document.createElement('button')
    $buttonRendezVous.setAttribute('id',
        `rendez-vous`)
    $buttonRendezVous.setAttribute('class',
        `m-1`)
    $buttonRendezVous.innerText = 'Demander un rendez-vous'


    $navDiv.append($buttonHome)
    $navDiv.append($buttonCreationDevis)
    $navDiv.append($buttonCreationCompte)
    $navDiv.append($buttonCreationCompteInterne)
    $navDiv.append($buttonVueBI)
    $navDiv.append($buttonRendezVous)
    //endregion

    //region HOME
    $('#home').click(function () {
        document.getElementById('main-content').innerHTML = ""
        let $mainDiv = document.getElementById('main-content')

    });
    //endregion

    //region CREATION-DEVIS
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
        let $selectClient = document.createElement('select')
        $selectClient.setAttribute('id', 'select-client')
        for (let i = 0; i < $clients.length; i++) {
            let $option = document.createElement('option')
            $option.setAttribute('value', $clients[i].id_client)
            $option.setAttribute('class', 'option-client')

            $option.innerText = $clients[i].mail
            $selectClient.append($option)
        }


        $topDevisDiv.append($labelNomDevis)
        $topDevisDiv.append($inputNomDevis)
        $topDevisDiv.append($selectClient)
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

        let $recapPiecesDiv = document.createElement('div')
        $recapPiecesDiv.setAttribute('id', 'recap-piece')
        $recapPiecesDiv.setAttribute('class', `container-fluid`)

        $centerLeftDevisDiv.append($buttonAjtPiece)
        $centerLeftDevisDiv.append($recapPiecesDiv)
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

        let $btnValiderDevis = document.createElement("button")
        $btnValiderDevis.setAttribute('id', 'valider-devis')
        $btnValiderDevis.setAttribute('type', 'button')
        $btnValiderDevis.innerText = "Créer"
        $bottomDevisDiv.append($btnValiderDevis)


        //endregion


        $devisDiv.append($topDevisDiv)
        $devisDiv.append($centerDevisDiv)
        $devisDiv.append($bottomDevisDiv)
        $devisForm.append($devisDiv)
        $mainDiv.append($devisForm)

        $('#valider-devis').click(function () {
            devisJSON["nom_devis"] = document.getElementById('nom').value
            for (let i = 0; i < devisJSON["pieces"].length; i++) {
                delete devisJSON["pieces"][i].id_front
            }
            devisJSON.prix = parseInt($pPriceDevis.innerText)
            var elem = document.getElementById('select-client')
            console.log(devisJSON)
            $.ajax({
                url: 'http://127.0.0.1:8000/create-devis/',
                type: 'post',
                contentType: 'application/json',
                data: JSON.stringify(devisJSON)
            }).done(function (msg, status, jqXHR) {
                console.log(msg)
                console.log(status)
                console.log(jqXHR)
            })
        })

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

                for (let i = 0; i < $products.length; i++) {
                    let $optGroup = document.createElement('optgroup')
                    $optGroup.setAttribute('label', $products[i].nom)
                    for (let j = 0; j < $products[i].modules.length; j++) {
                        let $option = document.createElement('option')
                        $option.setAttribute('value', $products[i].modules[j].id)
                        $option.setAttribute('class', 'option-module')

                        $option.innerText = $products[i].modules[j].nom
                        $optGroup.append($option)
                    }
                    $selectModule.append($optGroup)
                }
                $selectModuleDiv.append($selectModule)
                $centerPieceDiv.append($selectModuleDiv)
            });
            $('#valider-piece').click(function () {
                let piece = {
                    "nom": document.getElementById('piece-name').value,
                    "id_front": devisJSON["pieces"].length + 1,
                    "modules": []
                }
                let $prixTotal = 0
                for (i = 1; i < document.getElementById('center-piece-div').childElementCount + 1; i++) {

                    var elem = document.getElementById('select-module-' + i)
                    let module = {"id_module": parseInt(elem.value)}
                    piece["modules"].push(module)
                    for (let j = 0; j < $products.length; j++) {
                        for (let k = 0; k < $products[j].modules.length; k++) {
                            if ($products[j].modules[k].id === parseInt(elem.value)) {
                                $prixTotal += parseInt($products[j].modules[k].prix)
                            }
                        }
                    }
                }
                devisJSON["pieces"].push(piece)

                $pPriceDevis.innerText = $prixTotal + parseInt($pPriceDevis.innerText)
                let $recapPiecePrix = document.createElement('p')
                $recapPiecePrix.setAttribute('id', `prix-recap-piece-` + (devisJSON['pieces'].length))
                $recapPiecePrix.setAttribute('value', $prixTotal)
                $recapPiecePrix.innerText = $prixTotal
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
                $recapPieceDiv.append($recapPiecePrix)
                $recapPieceDiv.append($deleteBtnRecapPiece)
                $recapPiecesDiv.append($recapPieceDiv)
                DELETEPIECE.bind()
                document.getElementById('center-right-devis-div').innerHTML = ""
            });
        });
    });
    //endregion

    //region CREATION-COMPTE
    $('#creation-compte').click(function () {
        document.getElementById('main-content').innerHTML = ""
        let $mainDiv = document.getElementById('main-content')

    });
    //endregion

    //region CREATION-COMPTE-INTERNE
    $('#creation-compte-interne').click(function () {
        document.getElementById('main-content').innerHTML = ""
        let $mainDiv = document.getElementById('main-content')
        let $idTextAera = document.createElement('input')
        $idTextAera.setAttribute('type', 'number')
        $idTextAera.setAttribute('id', 'id-area')
        $idTextAera.setAttribute('name', 'id-area')
        let $labelIdTextAera = document.createElement('label')
        $labelIdTextAera.setAttribute('for', 'id-area')
        $labelIdTextAera.innerText = "ID ERP :"
        let $passwordAera = document.createElement('input')
        $passwordAera.setAttribute('type', 'password')
        $passwordAera.setAttribute('id', 'password-area')
        $passwordAera.setAttribute('name', 'password-area')

        let $labelPasswordAera = document.createElement('label')
        $labelPasswordAera.setAttribute('for', 'password-area')
        $labelPasswordAera.innerText = "PASSWORD :"

        let $btnCreateIU = document.createElement('button')
        $btnCreateIU.setAttribute('type', 'button')
        $btnCreateIU.setAttribute('id', 'create-internal-user')
        $btnCreateIU.innerText = "CREER"


        $mainDiv.append($labelIdTextAera)
        $mainDiv.append($idTextAera)
        $mainDiv.append($labelPasswordAera)
        $mainDiv.append($passwordAera)
        $mainDiv.append($btnCreateIU)

        $('#create-internal-user').click(function () {
            let $userInternalJSON = {
                "id": document.getElementById('id-area').value,
                "password": document.getElementById('password-area').value
            }
            $.ajax({
                url: 'http://127.0.0.1:8000/create-internal-user/',
                type: 'post',
                contentType: 'application/json',
                data: JSON.stringify($userInternalJSON)
            }).done(function (msg, status, jqXHR) {
                console.log(msg)
                console.log(status)
                console.log(jqXHR)
            })
        });
    });
    //endregion

    //region VUE-BI
    $('#vue-bi').click(function () {
        document.getElementById('main-content').innerHTML = ""
        let $mainDiv = document.getElementById('main-content')
        let $mainTopDiv = document.createElement('main-top-content')
        let $mainBottomDiv = document.createElement('main-bottom-content')
        $mainTopDiv.setAttribute('class', 'row')
        $mainBottomDiv.setAttribute('class', 'row')


        let $devisCreatedDiv = document.createElement('div')
        $devisCreatedDiv.setAttribute('class', 'col card bg-light m-3')
        $devisCreatedDiv.setAttribute('style', 'max-width: 400px;')

        let $devisCreatedHeaderDiv = document.createElement('div')
        $devisCreatedHeaderDiv.setAttribute('class', 'card-header')
        $devisCreatedHeaderDiv.innerText = "Tickets créés"
        let $devisCreatedBodyDiv = document.createElement('div')
        $devisCreatedBodyDiv.setAttribute('class', 'card-body')
        let $devisCreatedTitleDiv = document.createElement('div')
        $devisCreatedTitleDiv.setAttribute('class', 'card-title h1')
        $devisCreatedBodyDiv.append($devisCreatedTitleDiv)
        $devisCreatedDiv.append($devisCreatedHeaderDiv)
        $devisCreatedDiv.append($devisCreatedBodyDiv)
        $mainTopDiv.append($devisCreatedDiv)

        let $devisAcceptedDiv = document.createElement('div')
        $devisAcceptedDiv.setAttribute('class', 'col card text-white bg-success m-3')
        $devisAcceptedDiv.setAttribute('style', 'max-width: 400px;')
        let $devisAcceptedHeaderDiv = document.createElement('div')
        $devisAcceptedHeaderDiv.setAttribute('class', 'card-header')
        $devisAcceptedHeaderDiv.innerText = "Tickets créés"
        let $devisAcceptedBodyDiv = document.createElement('div')
        $devisAcceptedBodyDiv.setAttribute('class', 'card-body')
        let $devisAcceptedTitleDiv = document.createElement('div')
        $devisAcceptedTitleDiv.setAttribute('class', 'card-title h1')
        $devisAcceptedBodyDiv.append($devisAcceptedTitleDiv)
        $devisAcceptedDiv.append($devisAcceptedHeaderDiv)
        $devisAcceptedDiv.append($devisAcceptedBodyDiv)
        $mainTopDiv.append($devisAcceptedDiv)

        let $devisPendingDiv = document.createElement('div')
        $devisPendingDiv.setAttribute('class', 'col card text-white bg-warning m-3')
        $devisPendingDiv.setAttribute('style', 'max-width: 400px;')

        let $devisPendingHeaderDiv = document.createElement('div')
        $devisPendingHeaderDiv.setAttribute('class', 'card-header')
        $devisPendingHeaderDiv.innerText = "Tickets en attente"
        let $devisPendingBodyDiv = document.createElement('div')
        $devisPendingBodyDiv.setAttribute('class', 'card-body')
        let $devisPendingTitleDiv = document.createElement('div')
        $devisPendingTitleDiv.setAttribute('class', 'card-title h1')
        $devisPendingBodyDiv.append($devisPendingTitleDiv)
        $devisPendingDiv.append($devisPendingHeaderDiv)
        $devisPendingDiv.append($devisPendingBodyDiv)
        $mainBottomDiv.append($devisPendingDiv)

        let $devisCanceledDiv = document.createElement('div')
        $devisCanceledDiv.setAttribute('class', 'col card text-white bg-danger m-3')
        $devisCanceledDiv.setAttribute('style', 'max-width: 400px;')
        let $devisCanceledHeaderDiv = document.createElement('div')
        $devisCanceledHeaderDiv.setAttribute('class', 'card-header')
        $devisCanceledHeaderDiv.innerText = "Tickets refusées"
        let $devisCanceledBodyDiv = document.createElement('div')
        $devisCanceledBodyDiv.setAttribute('class', 'card-body')
        let $devisCanceledTitleDiv = document.createElement('div')
        $devisCanceledTitleDiv.setAttribute('class', 'card-title h1')
        $devisCanceledBodyDiv.append($devisCanceledTitleDiv)
        $devisCanceledDiv.append($devisCanceledHeaderDiv)
        $devisCanceledDiv.append($devisCanceledBodyDiv)
        $mainBottomDiv.append($devisCanceledDiv)

        $mainDiv.append($mainTopDiv)
        $mainDiv.append($mainBottomDiv)

        $.ajax({
            url: 'http://127.0.0.1:8000/get-devis/',
            type: 'get',
            dataType: 'json',
        }).done(function (data) {
            $devis = data.devis
            console.log($devis)
            $pendingCPT = 0
            $acceptedCPT = 0
            $refusedCPT = 0
            for (let i = 0; i < $devis.length; i++) {
                switch ($devis[i].etat) {
                    case 'En attente':
                        $pendingCPT++
                        break
                    case 'Accepté':
                        $acceptedCPT++
                        break
                    case 'Validé':
                        $refusedCPT++
                        break
                }
            }
            $devisCreatedTitleDiv.innerText = $pendingCPT + $acceptedCPT + $refusedCPT
            $devisAcceptedTitleDiv.innerText = $acceptedCPT
            $devisPendingTitleDiv.innerText = $pendingCPT
            $devisCanceledTitleDiv.innerText = $refusedCPT


        }).fail(function (data) {
            console.log('FAIL')
            console.log(data)
        })

    });
    //endregion

    //region VUE-BI
    $('#rendez-vous').click(function () {
        document.getElementById('main-content').innerHTML = ""

        let $mainDiv = document.getElementById('main-content')

    });
    //endregion
});
