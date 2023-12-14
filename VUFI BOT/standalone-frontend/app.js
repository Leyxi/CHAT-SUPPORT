let onSending = false

class Chatbox {
    constructor() {
        this.args = {
            openButton: document.querySelector('.chatbox__button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('#send__button'),
            botStatus: document.getElementById('bot__status')
        }

        this.state = false;
        this.messages = [];
    }

    display() {
        const { openButton, chatBox, sendButton, botStatus } = this.args;

        openButton.addEventListener('click', () => this.toggleState(chatBox))

        sendButton.addEventListener('click', () => this.onSendButton(chatBox))

        const node = chatBox.querySelector('input');
        node.addEventListener("keyup", async ({ key }) => {
            if (key === "Enter" && !onSending) {
                onSending = true
                botStatus.textContent = "AI is thinking..."
                sendButton.setAttribute("disabled", "true")
                sendButton.classList.add("disabled__send__button")
                await this.onSendButton(chatBox)
                sendButton.removeAttribute("disabled")
                sendButton.classList.remove("disabled__send__button")
                botStatus.textContent = "Online"
                onSending = false
            }
        })
    }

    toggleState(chatbox) {
        this.state = !this.state;

        // show or hide the box
        if (this.state) {
            chatbox.classList.add('chatbox--active')
        } else {
            chatbox.classList.remove('chatbox--active')
        }
    }

    async onSendButton(chatbox) {
        var textField = chatbox.querySelector('input');
        let text1 = textField.value
        if (text1 === "") {
            return;
        }

        let msg1 = { name: "User", message: text1 }
        this.messages.push(msg1);

        textField.value = ''
        this.updateChatText(chatbox)
        try {
            const res = await fetch(`http://127.0.0.1:5000/api?message=${text1}`, {
                method: 'GET',
                mode: 'cors'
            })
            const response = await res.json()
            let msg2 = { name: "Sam", message: response.response };
            this.messages.push(msg2);
            this.updateChatText(chatbox)
        } catch (error) {
            console.error('Error:', error);
            this.updateChatText(chatbox)
        }

    }

    updateChatText(chatbox) {
        var html = '';
        this.messages.slice().reverse().forEach(function (item, index) {
            if (item.name === "Sam") {
                html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>'
            } else {
                html += '<div class="messages__item messages__item--operator">' + item.message + '</div>'
            }
        });

        const chatmessage = chatbox.querySelector('.chatbox__messages');
        chatmessage.innerHTML = html;

        // Automatically scroll to the bottom
        chatmessage.scrollTop = chatmessage.scrollHeight;
    }
}

const chatbox = new Chatbox();
chatbox.display();
