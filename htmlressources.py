# Custom CSS to style the button
css = '''
<style>
.chat-message {
    padding: 1rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    background-color: #262730;
    transition: background 0.3s ease, box-shadow 0.3s ease;
}

.chat-message.user {
    background-color: #262730;
}

.chat-message.bot {
    background-color: #262730;
}

.chat-message .avatar {
    width: 12%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.chat-message .avatar img {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    object-fit: cover;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.chat-message .avatar img:hover {
    transform: scale(1.1);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.chat-message .message {
    width: 88%;
    padding: 0 1rem;
    color: #e0e0e0;
    font-size: 1rem;
    line-height: 1.5;
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://cdn.pixabay.com/photo/2021/01/04/10/37/icon-5887113_1280.png" alt="Bot Avatar">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://iconape.com/wp-content/files/mb/10833/png/iconfinder_1_avatar_2754574.png" alt="User Avatar">
    </div>    
    <div class="message">{{MSG}}</div>
</div>

'''