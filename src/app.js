function ldtemplate(tpl, name, img, desc) {
    axios.post('../router.php', {
        tpl: tpl,
        name: name,
        description: desc,
        img: img

    }).then((response) => {
        document.getElementById('template').innerHTML = response.data;
        initevents();
        initplugins();
    }, (error) => {
        console.log(error);
    });
}
function ldmodal(tpl, modalname) {
    axios.post('../router.php', {
        modal: tpl,
        modalname: modalname
    }).then((response) => {
        document.getElementById('modals').innerHTML = response.data;
        //launch chatbot 
        var modal = new bootstrap.Modal(document.getElementById(tpl))
        modal.show()
        if (tpl == 'chatbot') {
            initchatbot();
        }
    }, (error) => {
        console.log(error);
    });
}
function initplugins() {
    var venobox = new VenoBox();
}
function initevents() {
    const triggerElements = document.querySelectorAll('.pdf-trigger');
    const lightboxElement = document.querySelector('#pdf-lightbox');
    triggerElements.forEach(triggerElement => {
        triggerElement.addEventListener('click', (event) => {
            queryid = event.target.id;
            //Patch to chatGPT generated script: disable element before click 
            const boxes = document.querySelectorAll('#pdf-lightbox');
            boxes.forEach(box => {
                box.style.width = '100%';
            });
            //end patch
            const iframe = document.createElement('iframe');
            //this needs to be dynamic to the element index of the queryselectors ID
            //we can do this by differenting between class and ID, 
            //for the backend we can have the format of the ID [id].pdf
            iframe.setAttribute('src', '/uploads/' + queryid + '.pdf');

            lightboxElement.appendChild(iframe);
        });
    });

    lightboxElement.addEventListener('click', (event) => {
        if (event.target === lightboxElement) {
            closeLightbox();
        }
    });

    function closeLightbox() {
        //Patch to chatGPT script: disable element before click 
        const boxes = document.querySelectorAll('#pdf-lightbox');
        boxes.forEach(box => {
            box.style.width = '0%';
        });
        //end patch
        lightboxElement.innerHTML = '';
    }
}
function initchatbot() {
    document.getElementById('sendButton').addEventListener('click', (event) => {
        //apend to chat history
        var question = document.getElementById('userInput').value
        document.getElementById('hidebox').style.visibility = "hidden";
        document.getElementById('userInputLoading').style.visibility = "visible";

        document.getElementById('chat-history').insertAdjacentHTML("beforeend", '<div style="float:right;text-align:end;" class="chat-message user-message"><div style="padding-top: 10px;"><button class="btn btn-primary btn-sm">' + question + '</button></div>');
        //ping python server
        //This is the axious code: 
        //it still depends on jquery rn but i had a previous version since deleted 
        //which didn't use the append or $ function at all. 
        //  axios.post('http://127.0.0.1:3300/ajax', {
        //      question: question
        //  }).then((response) => {
        //                $('#chat-history').append('<div class="chat-message bot-message"><button class="btn btn-secondary btn-sm">' + response + '</button><br></div>');
        //  }, (error) => {
        //      console.log(error);
        //  });
        $.ajax({
            type: 'POST',
            url: 'http://127.0.0.1:3535/ajax',
            data: { question: question },
            success: function (response) {
                //reload sal animated and display response
                $('#chat-history').append('<div class=""><button class="chat-message bot-message btn btn-secondary btn-sm">' + response + '</button><br></div>');
                $('#userInput').val('');

                document.getElementById('hidebox').style.visibility = "visible";
                document.getElementById('userInputLoading').style.visibility = "hidden";


            },
            error: function (xhr, status, error) {
                // Handle errors
                console.log(error);
            }
        });
    })
}