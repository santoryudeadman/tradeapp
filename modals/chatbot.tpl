{{> modal-header}}
<div class="scrollbox" style="height:400px;width:100%;overflow:auto;" id="chat-history">
    <div class="chat-message">
        <button class="btn bot-message btn-secondary btn-sm">Hi, I am an AI Trading Assistant. How may I help you
            today?</button>
    </div>
</div>

<div id="userInputLoading" style="visibility:hidden;"><img src="uploads/uploads.gif" alt="Italian Trulli" style="width:25px;height:25px;"><h5>Processing...</h5></div>

<div id="hidebox" class="input-group mb-3">

    <input type="text" style="background:none;color:white;" class="form-control" placeholder="Type your message here"
        aria-label="Type your message here" id="userInput">
    <button class="btn btn-outline-secondary" type="button" id="sendButton">Send</button>
</div>
{{> modal-footer}}