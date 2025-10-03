def get_html_template():
    return """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <link rel="stylesheet" href="style.css" />
    <style>
    :root {
      --bodyBg: #0a0a0a;
      --bodyBg2: #1f1f1f;
      --bodyBg3: #3a3a3a;
      --bodyTxt: rgb(255 255 255 / 90%);
      --bodyTxt2: rgb(255 255 255 / 70%);
      --dominantBg: #222;
      --dominantBg2: #323232;
      --dominantBg3: #3e3e3e;
      --dominantTxt: rgb(255 255 255 / 90%);
      --dominantTxt2: rgb(255 255 255 / 70%);
      --accentBg: #03A9F4;
      --accentBg2: #0595d6;
      --accentTxt: #fff;
      --icoSize: 24px;
    }
      * {
        box-sizing: border-box;
      }

      html,
      body {
        margin: 0;
        padding: 0;
      }
      .icons_container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        align-items: center;
        column-gap: 24px;
        row-gap: 24px;
        padding: 16px;
        background: var(--bodyBg);
        
      }

      .icon_demo {
        display: flex;
        flex-direction: column;
        align-items: center;
        background: var(--bodyBg2);
        border: 1px solid var(--bodyBg3);
        row-gap: 6px;
        border-radius: 12px;
        padding: 12px;
        transition: all 0.3s;
        cursor: pointer;
        overflow: hidden;
      }

      .card-client {
        background: var(--dominantBg);
        color: var(--dominantTxt);
        width: 13rem;
        padding-top: 25px;
        padding-bottom: 25px;
        padding-left: 20px;
        padding-right: 20px;
        border: 4px solid var(--dominantBg3);
        border-radius: 8px;
        text-align: center;
        font-family: "Poppins", sans-serif;
        transition: all 0.3s ease;
        align-items: center;
        display: flex;
        flex-direction: column;
      }

      .card-client:hover {
        transform: translateY(-10px);
      }

      .name-client{
       display: flex;
       align-items: center;
       flex-direction: column;
       row-gap: 4px; 
      }

      .name-text{
        color: var(--dominantTxt2);
      }

      .icon_main {
        overflow: hidden;
        object-fit: cover;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        margin: auto;
        opacity: 1;
        transition: all 0.2s;
      }

      .icon_old,
      .icon_main{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
      }

      .icon_preview{
        width: 5rem;
        height: 5rem;
        position: relative;
      }

      .icon_main > i {
        --icoSize: 80px;
        fill: currentColor;
      }
      
      html {
        background: var(--bodyBg);
        color: var(--bodyTxt);
        font-family: Arial;
      }

      .icon_demo_row {
        display: flex;
        align-items: center;
        justify-content: space-between;
      }

      .icon_demo_row_cont {
        margin-bottom: 8px;
      }

      .icon_demo_row_cont::before {
        content: "";
        display: block;
        width: 100%;
        height: 2px;
        margin: 20px 0;
        background: #7cdacc;
      }

      .btn_demo_row {
        display: flex;
        align-items: center;
        column-gap: 16px;
      }

      .btn_demo {
        width: 100%;
        position: relative;
        padding: 10px 22px;
        border-radius: 6px;
        border: none;
        color: var(--accentTxt);
        cursor: pointer;
        background-color: var(--accentBg);
        transition: all 0.2s ease;
        text-transform: capitalize;
        font-weight: 700;
        
      }

      .btn_demo:active {
        transform: scale(0.96);
      }

      .btn_demo:before,
      .btn_demo:after {
        position: absolute;
        content: "";
        width: 150%;
        left: 50%;
        height: 100%;
        transform: translateX(-50%);
        z-index: -1000;
        background-repeat: no-repeat;
      }

      .btn_demo:hover:before {
        top: -70%;
        background-image: radial-gradient(
            circle,
            var(--dominantBg) 20%,
            transparent 20%
          ),
          radial-gradient(
            circle,
            transparent 20%,
            var(--dominantBg) 20%,
            transparent 30%
          ),
          radial-gradient(circle, var(--dominantBg) 20%, transparent 20%),
          radial-gradient(circle, var(--dominantBg) 20%, transparent 20%),
          radial-gradient(
            circle,
            transparent 10%,
            var(--dominantBg) 15%,
            transparent 20%
          ),
          radial-gradient(circle, var(--dominantBg) 20%, transparent 20%),
          radial-gradient(circle, var(--dominantBg) 20%, transparent 20%),
          radial-gradient(circle, var(--dominantBg) 20%, transparent 20%),
          radial-gradient(circle, var(--dominantBg) 20%, transparent 20%);
        background-size: 10% 10%, 20% 20%, 15% 15%, 20% 20%, 18% 18%, 10% 10%,
          15% 15%, 10% 10%, 18% 18%;
        background-position: 50% 120%;
        animation: greentopBubbles 0.6s ease;
      }

      @keyframes greentopBubbles {
        0% {
          background-position: 5% 90%, 10% 90%, 10% 90%, 15% 90%, 25% 90%,
            25% 90%, 40% 90%, 55% 90%, 70% 90%;
        }

        50% {
          background-position: 0% 80%, 0% 20%, 10% 40%, 20% 0%, 30% 30%, 22% 50%,
            50% 50%, 65% 20%, 90% 30%;
        }

        100% {
          background-position: 0% 70%, 0% 10%, 10% 30%, 20% -10%, 30% 20%,
            22% 40%, 50% 40%, 65% 10%, 90% 20%;
          background-size: 0% 0%, 0% 0%, 0% 0%, 0% 0%, 0% 0%;
        }
      }

      .btn_demo:active::after {
        bottom: -70%;
        background-image: radial-gradient(
            circle,
            var(--dominantBg) 20%,
            transparent 20%
          ),
          radial-gradient(circle, var(--dominantBg) 20%, transparent 20%),
          radial-gradient(
            circle,
            transparent 10%,
            var(--dominantBg) 15%,
            transparent 20%
          ),
          radial-gradient(circle, var(--dominantBg) 20%, transparent 20%),
          radial-gradient(circle, var(--dominantBg) 20%, transparent 20%),
          radial-gradient(circle, var(--dominantBg) 20%, transparent 20%),
          radial-gradient(circle, var(--dominantBg) 20%, transparent 20%);
        background-size: 15% 15%, 20% 20%, 18% 18%, 20% 20%, 15% 15%, 20% 20%,
          18% 18%;
        background-position: 50% 0%;
        animation: greenbottomBubbles 0.6s ease;
      }

      @keyframes greenbottomBubbles {
        0% {
          background-position: 10% -10%, 30% 10%, 55% -10%, 70% -10%, 85% -10%,
            70% -10%, 70% 0%;
        }

        50% {
          background-position: 0% 80%, 20% 80%, 45% 60%, 60% 100%, 75% 70%,
            95% 60%, 105% 0%;
        }

        100% {
          background-position: 0% 90%, 20% 90%, 45% 70%, 60% 110%, 75% 80%,
            95% 70%, 110% 10%;
          background-size: 0% 0%, 0% 0%, 0% 0%, 0% 0%, 0% 0%;
        }
      }

      .message {
        display: none;
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: black;
        color: white;
        padding: 10px;
        border-radius: 5px;
      }
    </style>
  </head>
  <body>
    <div class="icons_container">
"""
