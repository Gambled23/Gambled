age: int = 21

projects = {
    "asanawave": {
        "avatar":"/asanawave/logo.svg",
        "title":"Asanawave",
        "description_short":"Webapp django app for a yoga teacher",
        "description_long":"Currently I’m working with a three people team to develop and deploy a webapp for a private client, using Django as backend and HTMX to replace Javascript in the frontend.\nWe provide a space for a private teachers to upload lessons and manage all of their learning materials, while keeping close communication with their students.\nMy main responsibilities as a developer are integrating newly developed components to the system, write tests for existing components, and as a server administrator to provide a seamless integration on cloud.",
        "link":"https://asanawave.com/",
        "repo":"",
        "body_image":"/asanawave/1.png",
        "technologies":["django", "htmx & hyperscript", "mariadb", "docker", "nginx", "oracle cloud", "machine learning", "webhosting", "selfhost"],
    },

    "nix-dotfiles": {
        "avatar":"/logos/nix.png",
        "title":"Nix dotfiles",
        "description_short":"My nix configuration for all my devices",
        "description_long":"All of my devices run NixOS, so I decided to create a repository with all of my dotfiles and configuration files.\nI use this repository to keep track of all the changes I make to my system, and to share my configuration with others.\nFeel free to snoop around.",
        "link":"",
        "repo":"https://github.com/Gambled23/nix-dotfiles",
        "body_image":"",
        "technologies":["nix", "nixos", "home-manager", "bash"],
    },

    "dixios": {
        "avatar":"/dixios/logo.svg",
        "title":"Dixios",
        "description_short":"AI and LLM Consultant at Dixios",
        "description_long":"I'm currently working as a consultant for Dixios, a company that gives training to office employees on how to use AI tools to improve their productivity.\nMy main responsibilities are to create training materials, and to give training sessions to employees.\nI also help the company to integrate AI tools into their workflow, and to create custom solutions for their clients.\n\nFun fact: I worked as a fullstack dev for the webpage too.",
        "link":"https://dixios.com/",
        "repo":"",
        "body_image":"/dixios/1.png",
        "technologies":["html", "css", "bootstrap", "webhosting",],
    },

    "nisha": {
        "avatar":"/nisha/logo.ico",
        "title":"Nisha",
        "description_short":"Crochet and knitting e-commerce",
        "description_long":"Nisha is a small e-commerce that sells crochet plushies and knitted decorations.\nHere I worked as a fullstack webdev creating a cozy yet elegant experience for the users browsing the store.\nEverything here was selfhosted on a rpi4 using nginx and mariadb.\nSadly, the store is no longer active, but you can still check the code on the repository.",
        "link":"",
        "repo":"https://github.com/Gambled23/TheNishaProject",
        "body_image":"",
        "technologies":["laravel", "livewire", "php", "html", "css", "tailwind", "mariadb", "docker", "nginx", "webhosting", "selfhost"],
    },

    "eliasbot": {
        "avatar":"/eliasbot/logo.svg",
        "title":"Eliasbot",
        "description_short":"Discord bot for a private server",
        "description_long":"Self hosted on a raspberry pi, I made this bot using Hikari, a python API for Discord bots, it have some funny commands like quote the bible, birthday celebrations, calling all members, and even play some music using the spotify api.\nJust a silly project I made for my discord server.",
        "link":"",
        "repo":"",
        "body_image":"",
        "technologies":["python", "hikari", "selfhost"],
    },    
    
    "caphpibot": {
        "avatar":"/caphpibot/logo.svg",
        "title":"Caphpibot",
        "description_short":"ElCapibe's discord bot",
        "description_long":"My second time building a discord bot, this time using Laracord, a Laravel forked microframework for building discord bots.\nThis bot was used to manage 'La capibanda', El Capibe's league of legends community server\nIt had commands to interact with the influencer, vote for next video ideas, play games in discord, connect your League of legends account, and some moderation commands to automate the server.\nWhen the server grew too big, I decided to stop maintaining the bot and the moderators switched to other automod bots, but it was a fun experience.\n",
        "link":"",
        "repo":"",
        "body_image":"",
        "technologies":["laravel", "laracord", "php"],
    },

    "TheParkingZone": {
        "avatar":"/theparkingzone/logo.ico",
        "title":"The Parking Zone",
        "description_short":"GUI for complete parking lot administration, including QR code I/O and ticket printing",
        "description_long":"A system for parking-spaces administration, auto-assigning the nearest available space, and printing a QR code with the assigned space.\nMade entirely using python, this project uses tkinter to give the admin an easy to use GUI\nAs an administrator, you can watch live status of the parking lot, receive notifications from cars parked for more than 48 hours, create and delete parking spaces, and everything you would expect from a parking lot administration software.\nThe software runs entirely on the local PC using a self-hosted postgres database, but thanks to the GUI the administrator user doesn't need to know anything about databases to fully use The parking zone.",
        "link":"",
        "repo":"https://github.com/Gambled23/The-Parking-Zone",
        "body_image":"",
        "technologies":["python", "tkinter", "opencv", "postgresql"],
    },

    "OnlineWeddingInvitation": {
        "avatar":"/wedding/logo.svg",
        "title":"Online Wedding Invitation",
        "description_short":"Hosted online wedding invitation for a private client",
        "description_long":"A project for a private client, the client wanted to have an online invitation for their wedding, so they could send the link to everyone invited instead of waiting for the cards to arrive to each guest.\nI deployed for a private client a modified version of dewanakl’s online wedding invitation, the invitation was fully accesible on the web until after the wedding day\nIt has a countdown for the wedding day and some important details about the event like the location or exact time.\nThe client was very happy with the result, and I was happy to help them with their wedding.",
        "link":"",
        "repo":"https://github.com/Gambled23/undangan",
        "body_image":"",
        "technologies":["html", "css", "js", "webhosting"],
    },

    "Gambled23": {
        "avatar":"/favicon.ico",
        "title":"Personal website",
        "description_short":"You're looking at it!",
        "description_long":"My personal webpage, I made this using pure python thanks to Reflex\nThis started like an experiment of me trying to recreate my (now old) personal landingpage buit with just html and css, but without actually writing any html or css.\nThis project helped me learn a lot about reflex, and how you can use it to create a fullstack webapp at a really good speed.\n\nAnd now as I write this the card reloads and words appear on the screen, some wizardy happens here.\n",
        "link":"",
        "repo":"https://github.com/Gambled23/Gambled",
        "body_image":"",
        "technologies":["python", "reflex", "css", "webhosting"],
    },
}