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

const ACCEPTERDEVIS = {
    bind() {
        $(".button-accept-devis").attr('class', 'button-accept-devis btn btn-success m-1').click(function () {
            console.log($(this))

            let elem = document.getElementById($(this).attr('id'))
            console.log(elem)

            let lio = elem.id.lastIndexOf('-');
            let idDevis = elem.id.slice(lio + 1);
            console.log(idDevis)

            //NE PAS OUBLIER DE CHANGER LA SPAN

            //JSON.stringify({'id': idDevis})
            $.ajax({
                url: 'http://127.0.0.1:8000/accept-devis/',
                type: 'post',
                contentType: 'application/json',
                data: JSON.stringify({'id': idDevis}),
            }).done(function (msg, status, jqXHR) {
                /*    console.log(msg)
                    console.log(status)
                    console.log(jqXHR)*/
                $products = msg
                let $span = document.getElementById('status-devis-' + idDevis)
                $span.setAttribute('class', 'ml-2 badge badge-success')
                $span.innerText = 'Accepté'

                let idBtnAccept = '#button-accept-devis-' + idDevis
                let idBtnCancel = '#button-cancel-devis-' + idDevis
                $(idBtnAccept).hide()
                $(idBtnCancel).hide()

            })
        });
    }
};

const REFUSERDEVIS = {
    bind() {
        $(".button-cancel-devis").attr('class', 'button-cancel-devis btn btn-danger m-1').click(function () {
            console.log($(this))

            let elem = document.getElementById($(this).attr('id'))
            console.log(elem)

            let lio = elem.id.lastIndexOf('-');
            let idDevis = elem.id.slice(lio + 1);
            console.log(idDevis)

            $.ajax({
                url: 'http://127.0.0.1:8000/cancel-devis/',
                type: 'post',
                contentType: 'application/json',
                data: JSON.stringify({'id': idDevis}),
            }).done(function (msg, status, jqXHR) {
                /*    console.log(msg)
                    console.log(status)
                    console.log(jqXHR)*/
                $products = msg
                let $span = document.getElementById('status-devis-' + idDevis)
                $span.setAttribute('class', 'ml-2 badge badge-danger')
                $span.innerText = 'Refusé'

                let idBtnAccept = '#button-accept-devis-' + idDevis
                let idBtnCancel = '#button-cancel-devis-' + idDevis
                let idBtnAddPlan = '#button-add-plan-devis-' + idDevis
                $(idBtnAccept).hide()
                $(idBtnCancel).hide()
                $(idBtnAddPlan).hide()
            })
        });
    }
};

const SENDFILE = {
    bind() {
        $(".button-send-file-devis").attr('class', 'm-1 btn btn-success button-send-file-devis').click(function () {
            //console.log($(this))

            let elem = document.getElementById($(this).attr('id'))
            //console.log(elem)

            let lio = elem.id.lastIndexOf('-');
            let idDevis = elem.id.slice(lio + 1);
            let btnSendFile = ('button-send-file-devis-' + idDevis)
            let btnSelectFile = ('input-select-file-devis-' + idDevis)
            let file = document.getElementById(btnSelectFile)
            file.files[0].name = idDevis + '-' + file.files[0].name
            let formData = new FormData();
            formData.append('file.pdf', file.files[0]);
            var xhr = new XMLHttpRequest();
            xhr.onload = function (e) {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    //Après le send on passe ici si 200
                    //button-div-devis-2
                    let divToHide = '#button-div-devis-' + idDevis
                    $(divToHide).hide()
                    result = xhr.responseText;
                    result_parsed = JSON.parse(result)
                    let id_plan = result_parsed.id_plan
                    data_json = {"id_plan": id_plan, "id_devis": parseInt(idDevis)}
                    $.ajax({
                        url: 'http://127.0.0.1:8000/add-plan-to-devis/',
                        type: 'post',
                        data: JSON.stringify(data_json),
                        dataType: 'application/json',
                    }).done(function (msg, status, jqXHR) {
                        /*    console.log(msg)
                            console.log(status)
                            console.log(jqXHR)*/

                    })

                }
            }
            xhr.open('POST', "http://127.0.0.1:8000/send-plan/", true);
            xhr.setRequestHeader("Authorization", "");
            xhr.send(formData);
        });
    }
};

const AJOUTPLAN = {
    bind() {
        $(".button-add-plan-devis").attr('class', 'button-add-plan-devis btn btn-info').click(function () {
            //console.log($(this))

            let elem = document.getElementById($(this).attr('id'))
            //console.log(elem)

            let lio = elem.id.lastIndexOf('-');
            let idDevis = elem.id.slice(lio + 1);
            let $buttonsDiv = document.getElementById('button-div-devis-' + idDevis)
            let $inputSelectFile = document.createElement('input')
            $inputSelectFile.setAttribute('id', ('input-select-file-devis-' + idDevis))
            $inputSelectFile.setAttribute('class', ('m-1 input-select-file-devis' + idDevis))
            $inputSelectFile.setAttribute('type', 'file')
            $inputSelectFile.setAttribute('accept', '.pdf')

            let $btnSendFile = document.createElement('button')
            $btnSendFile.setAttribute('id', ('button-send-file-devis-' + idDevis))
            $btnSendFile.setAttribute('class', 'm-1 btn btn-success button-send-file-devis')
            $btnSendFile.setAttribute('type', 'button')
            $btnSendFile.innerText = 'Valider'

            $buttonsDiv.append($inputSelectFile)
            $buttonsDiv.append($btnSendFile)
            SENDFILE.bind()
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

    let $buttonLogin = document.createElement('button')
    $buttonLogin.setAttribute('id',
        `login`)
    $buttonLogin.setAttribute('class',
        `m-1`)
    $buttonLogin.innerText = 'Connexion'

    $navDiv.append($buttonHome)
    $navDiv.append($buttonCreationDevis)
    $navDiv.append($buttonCreationCompte)
    $navDiv.append($buttonCreationCompteInterne)
    $navDiv.append($buttonVueBI)
    $navDiv.append($buttonLogin)
    //endregion

    //region HOME
    $('#home').click(function () {
        document.getElementById('main-content').innerHTML = ""
        // RECUPERER MAIL DE L'USER CO POUR R2CUPERER LA LISTE DES DEVIS OU IL EST IMPLIQUER
        // SI USER BE RECUPERER TOUT DEVIS

        user = {
            "mail": "test@test.fr"
        }

        $.ajax({
            url: 'http://127.0.0.1:8000/get-devis/',
            type: 'get',
            contentType: 'application/json',
            data: user
        }).done(function (data, status, jqXHR) {
            /*    console.log(msg)
                console.log(status)
                console.log(jqXHR)*/
            $devis = data.devis
            console.log($devis)
            let $mainDiv = document.getElementById('main-content')
            for (let i = 0; i < $devis.length; i++) {
                let $devisDiv = document.createElement('div')
                $devisDiv.setAttribute('id', ('devis-' + $devis[i].id_devis))
                $devisDiv.setAttribute('class', 'container-fluid border rounded border-dark bg-dark m-4')
                let $devisTopDiv = document.createElement('div')
                $devisTopDiv.setAttribute('id', ('top-devis-' + $devis[i].id_devis))
                $devisTopDiv.setAttribute('class', 'row rounded bg-dark text-white')
                let $devisMidDiv = document.createElement('div')
                $devisMidDiv.setAttribute('id', ('mid-devis-' + $devis[i].id_devis))
                $devisMidDiv.setAttribute('class', 'row rounded bg-light')

                let $titleDevis = document.createElement('h1')
                $titleDevis.setAttribute('id', ('title-devis-' + $devis[i].id_devis))
                $titleDevis.setAttribute('class', 'h4 m-2')
                $titleDevis.innerText = $devis[i].nom_devis

                let $statusDevis = document.createElement('span')
                $statusDevis.setAttribute('id', ('status-devis-' + $devis[i].id_devis))
                switch ($devis[i].etat) {
                    case 'En attente':
                        $statusDevis.setAttribute('class', 'ml-2 badge badge-warning')
                        break
                    case 'Accepté':
                        $statusDevis.setAttribute('class', 'ml-2 badge badge-success')
                        break
                    case 'Refusé':
                        $statusDevis.setAttribute('class', 'ml-2 badge badge-danger')
                        break
                }
                $statusDevis.innerText = $devis[i].etat

                let $priceDiv = document.createElement('div')
                $priceDiv.setAttribute('id', ('price-div-devis-' + $devis[i].id_devis))
                $priceDiv.setAttribute('class', 'col')

                let $price = document.createElement('p')
                $price.setAttribute('id', ('price-devis-' + $devis[i].id_devis))
                $price.innerText = $devis[i].prix + '€'

                let $buttonDevisDiv = document.createElement('div')
                $buttonDevisDiv.setAttribute('id', ('button-div-devis-' + $devis[i].id_devis))
                $buttonDevisDiv.setAttribute('class', 'col')


                if ($devis[i].etat === 'En attente') {
                    let $buttonAcceptDevis = document.createElement('button')
                    $buttonAcceptDevis.setAttribute('id', ('button-accept-devis-' + $devis[i].id_devis))
                    $buttonAcceptDevis.setAttribute('class', 'button-accept-devis btn btn-success m-1')
                    $buttonAcceptDevis.setAttribute('type', 'button')
                    $buttonAcceptDevis.innerText = "Accepter"

                    let $buttonCancelDevis = document.createElement('button')
                    $buttonCancelDevis.setAttribute('id', ('button-cancel-devis-' + $devis[i].id_devis))
                    $buttonCancelDevis.setAttribute('class', 'button-cancel-devis btn btn-danger m-1')
                    $buttonCancelDevis.setAttribute('type', 'button')
                    $buttonCancelDevis.innerText = "Refuser"
                    $buttonDevisDiv.append($buttonAcceptDevis)
                    $buttonDevisDiv.append($buttonCancelDevis)
                }

                let $buttonModifyDevis = document.createElement('button')
                $buttonModifyDevis.setAttribute('id', ('button-mofify-devis-' + $devis[i].id_devis))
                $buttonModifyDevis.setAttribute('class', 'button-modify-devis btn btn-primary m-1')
                $buttonModifyDevis.setAttribute('type', 'button')
                $buttonModifyDevis.innerText = "Modifier"
                $buttonDevisDiv.append($buttonModifyDevis)

                if ($devis[i].plan === null && ($devis[i].etat === "En attente" || $devis[i].etat === "Accepté")) {
                    let $buttonAddPlanDevis = document.createElement('button')
                    $buttonAddPlanDevis.setAttribute('id', ('button-add-plan-devis-' + $devis[i].id_devis))
                    $buttonAddPlanDevis.setAttribute('class', 'button-add-plan-devis btn btn-info m-1')
                    $buttonAddPlanDevis.setAttribute('type', 'button')
                    $buttonAddPlanDevis.innerText = "Ajouter plan"
                    $buttonDevisDiv.append($buttonAddPlanDevis)
                }
                $priceDiv.append($price)
                $devisMidDiv.append($priceDiv)
                $devisMidDiv.append($buttonDevisDiv)
                $titleDevis.append($statusDevis)
                $devisTopDiv.append($titleDevis)
                $devisDiv.append($devisTopDiv)
                $devisDiv.append($devisMidDiv)
                $mainDiv.append($devisDiv)

            }
            ACCEPTERDEVIS.bind()
            REFUSERDEVIS.bind()
            AJOUTPLAN.bind()
        })
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
        let $createClientTopDiv = document.createElement('div')
        $createClientTopDiv.setAttribute('id', 'createClientTopDiv')
        let $createClientBottomDiv = document.createElement('div')
        $createClientBottomDiv.setAttribute('id', 'createClientBottomDiv')

        let $isExistClientCheckbox = document.createElement('input')
        $isExistClientCheckbox.setAttribute('id', 'isExistClientCheckbox')
        $isExistClientCheckbox.setAttribute('type', 'checkbox')
        $isExistClientCheckbox.setAttribute('name', 'isExistClientCheckbox')
        let $labelIsExistClientCheckbox = document.createElement('label')
        $labelIsExistClientCheckbox.setAttribute('for', 'isExistClientCheckbox')
        $labelIsExistClientCheckbox.innerText = "Je suis déjà client Madera"

        let $createClientButton = document.createElement('button')
        $createClientButton.setAttribute('id', 'createClientButton')
        $createClientButton.setAttribute('type', 'button')
        $createClientButton.innerText = "Créer compte"

        let $lnDiv = document.createElement('div')
        let $fnDiv = document.createElement('div')
        let $adrDiv = document.createElement('div')
        let $emDiv = document.createElement('div')
        let $pnDiv = document.createElement('div')
        let $pwDiv = document.createElement('div')
        let $cbDiv = document.createElement('div')

        let $eMailArea = document.createElement('input')
        $eMailArea.setAttribute('id', 'eMailArea')
        $eMailArea.setAttribute('type', 'mail')
        $eMailArea.setAttribute('name', 'eMailArea')
        $eMailArea.setAttribute('maxlength', 50)
        let $labelEMailArea = document.createElement('label')
        $labelEMailArea.setAttribute('for', 'eMailArea')
        $labelEMailArea.innerText = "Adresse mail"

        let $passwordArea = document.createElement('input')
        $passwordArea.setAttribute('id', 'passwordArea')
        $passwordArea.setAttribute('type', 'password')
        $passwordArea.setAttribute('name', 'passwordArea')
        let $labelPasswordArea = document.createElement('label')
        $labelPasswordArea.setAttribute('for', 'passwordArea')
        $labelPasswordArea.innerText = "Password"

        let $lastnameArea = document.createElement('input')
        $lastnameArea.setAttribute('id', 'lastnameArea')
        $lastnameArea.setAttribute('type', 'text')
        $lastnameArea.setAttribute('name', 'lastnameArea')
        $lastnameArea.setAttribute('maxlength', 25)
        let $labelLastnameArea = document.createElement('label')
        $labelLastnameArea.setAttribute('for', 'lastnameArea')
        $labelLastnameArea.innerText = "Nom"

        let $firstnameArea = document.createElement('input')
        $firstnameArea.setAttribute('id', 'firstnameArea')
        $firstnameArea.setAttribute('type', 'text')
        $firstnameArea.setAttribute('name', 'firstnameArea')
        $firstnameArea.setAttribute('maxlength', 25)
        let $labelFirstnameArea = document.createElement('label')
        $labelFirstnameArea.setAttribute('for', 'firstnameArea')
        $labelFirstnameArea.innerText = "Prenom"

        let $addressArea = document.createElement('textarea')
        $addressArea.setAttribute('id', 'addressArea')
        $addressArea.setAttribute('type', 'textarea')
        $addressArea.setAttribute('name', 'addressArea')
        $addressArea.setAttribute('maxlength', 250)
        let $labelAddressArea = document.createElement('label')
        $labelAddressArea.setAttribute('for', 'addressArea')
        $labelAddressArea.innerText = "Adresse"

        let $phoneNumberArea = document.createElement('input')
        $phoneNumberArea.setAttribute('id', 'phoneNumberArea')
        $phoneNumberArea.setAttribute('type', 'tel')
        $phoneNumberArea.setAttribute('name', 'phoneNumberArea')
        $phoneNumberArea.setAttribute('maxlength', 10)
        let $labelNumberArea = document.createElement('label')
        $labelNumberArea.setAttribute('for', 'phoneNumberArea')
        $labelNumberArea.innerText = "Téléphone"

        $emDiv.append($labelEMailArea)
        $emDiv.append($eMailArea)
        $pwDiv.append($labelPasswordArea)
        $pwDiv.append($passwordArea)
        $cbDiv.append($isExistClientCheckbox)
        $cbDiv.append($labelIsExistClientCheckbox)

        $createClientTopDiv.append($emDiv)
        $createClientTopDiv.append($pwDiv)
        $createClientTopDiv.append($cbDiv)

        $lnDiv.append($labelLastnameArea)
        $lnDiv.append($lastnameArea)
        $fnDiv.append($labelFirstnameArea)
        $fnDiv.append($firstnameArea)
        $adrDiv.append($labelAddressArea)
        $adrDiv.append($addressArea)
        $pnDiv.append($labelNumberArea)
        $pnDiv.append($phoneNumberArea)

        $createClientBottomDiv.append($lnDiv)
        $createClientBottomDiv.append($fnDiv)
        $createClientBottomDiv.append($adrDiv)
        $createClientBottomDiv.append($pnDiv)

        $mainDiv.append($createClientTopDiv)
        $mainDiv.append($createClientBottomDiv)
        $mainDiv.append($createClientButton)

        $('#isExistClientCheckbox').click(function () {
            let checkbox = document.getElementById('isExistClientCheckbox')
            console.log(checkbox.checked)
            if (checkbox.checked) {
                $('#createClientBottomDiv').hide()
            } else {
                $('#createClientBottomDiv').show()
            }
        });

        $('#createClientButton').click(function () {
            data_json = {}
            let checkbox = document.getElementById('isExistClientCheckbox')
            let mail = document.getElementById('eMailArea')
            let password = document.getElementById('passwordArea')
            let lastname = document.getElementById('lastnameArea')
            let firstname = document.getElementById('firstnameArea')
            let address = document.getElementById('addressArea')
            let phonenumber = document.getElementById('phoneNumberArea')

            if (checkbox.checked) {
                data_json = {
                    "isClientExist": checkbox.checked,
                    "email": mail.value,
                    "password": password.value,
                }
            } else {
                data_json = {
                    "isClientExist": checkbox.checked,
                    "email": mail.value,
                    "password": password.value,
                    "lastname": lastname.value,
                    "firstname": firstname.value,
                    "address": address.value,
                    "phonenumber": phonenumber.value
                }
            }
            console.log(data_json)
        });
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
    $('#login').click(function () {
        document.getElementById('main-content').innerHTML = ""
        let $mainDiv = document.getElementById('main-content')

        let $eMailArea = document.createElement('input')
        $eMailArea.setAttribute('id', 'eMailArea')
        $eMailArea.setAttribute('type', 'mail')
        $eMailArea.setAttribute('name', 'eMailArea')
        $eMailArea.setAttribute('maxlength', 50)
        let $labelEMailArea = document.createElement('label')
        $labelEMailArea.setAttribute('for', 'eMailArea')
        $labelEMailArea.innerText = "Adresse mail"

        let $passwordArea = document.createElement('input')
        $passwordArea.setAttribute('id', 'passwordArea')
        $passwordArea.setAttribute('type', 'password')
        $passwordArea.setAttribute('name', 'passwordArea')
        let $labelPasswordArea = document.createElement('label')
        $labelPasswordArea.setAttribute('for', 'passwordArea')
        $labelPasswordArea.innerText = "Password"

        let $ConnexionButton = document.createElement('button')
        $ConnexionButton.setAttribute('id', 'connexionButton')
        $ConnexionButton.setAttribute('type', 'button')
        $ConnexionButton.innerText = "Connexion"

        let $emDiv = document.createElement('div')
        let $pwDiv = document.createElement('div')

        $emDiv.append($labelEMailArea)
        $emDiv.append($eMailArea)

        $pwDiv.append($labelPasswordArea)
        $pwDiv.append($passwordArea)

        $mainDiv.append($emDiv)
        $mainDiv.append($pwDiv)
        $mainDiv.append($ConnexionButton)

        $('#connexionButton').click(function () {
            email = document.getElementById('eMailArea')
            password = document.getElementById('passwordArea')
            data_json = {"email": email.value, "password": password.value}
            console.log(data_json)
            $.ajax({
                url: 'http://127.0.0.1:8000/manual-api-auth/login/',
                type: 'post',
                data: JSON.stringify(data_json),
                dataType: 'json',
            }).done(function (msg, status, jqXHR) {
                console.log('test')
                console.log(status)
                console.log(jqXHR)
            }).fail(function (msg, status, jqXHR) {
                console.log('fail')
                console.log(msg)
                console.log(status)
                console.log(jqXHR)
            })
        });
    });
});
