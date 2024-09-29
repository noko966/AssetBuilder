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
        --bodyBg: #091d2b;
        --bodyBg2: #141f27;
        --bodyBg3: #445c6f;
        --bodyTxt: rgba(255,255,255,0.9);
        --bodyTxt2: rgba(255,255,255,0.6);
        --dominantBg: #0b293d;
        --dominantBg2: #14496d;
        --dominantBg3: #286a96;
        --dominantTxt: rgba(255,255,255,0.9);
        --dominantTxt2: rgba(255,255,255,0.6);
        --accentBg: #157c82;
        --accentBg2: #33454d;
        --accentTxt: #fff;
        --icoSize: 24px;
    }
      * {
        box-sizing: border-box;
      }

      @font-face {
            font-family: "digiSportIcons";
            src: url("https://cdn-sp.totogaming.am/assets/fonts/sport-icons/sportsIcons.eot?v100");
            src: url(".https://cdn-sp.totogaming.am/assets/fonts/sport-icons/sportsIcons.eot?#iefix&v100") format("embedded-opentype"),
                url("https://cdn-sp.totogaming.am/assets/fonts/sport-icons/sportsIcons.woff2?v100") format("woff2"),
                url("https://cdn-sp.totogaming.am/assets/fonts/sport-icons/sportsIcons.woff?v100") format("woff"),
                url("https://cdn-sp.totogaming.am/assets/fonts/sport-icons/sportsIcons.ttf?v100") format("truetype");
            font-weight: 900;
            font-style: normal;
            font-display: block;
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
        width: 5rem;
        height: 5rem;
        border: 4px solid var(--dominantBg2);
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        margin: auto;
        opacity: 1;
        transition: all 0.2s;
      }

      .icon_main:hover{
        opacity: 0;
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
        font-size: var(--icoSize);
        line-height: var(--icoSize);
        width: var(--icoSize);
        height: var(--icoSize);
      }
      
      .icon_old > i {
        --icoSize: 80px;
        fill: currentColor;
        font-size: var(--icoSize);
        line-height: var(--icoSize);
        width: var(--icoSize);
        height: var(--icoSize);
        font-weight: 900;
        color: var(--dominantTxt2);
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

def get_css_template(FONT_FILE_NAME, FONT_FAMILY_NAME, V ):

  
  return f"""
[class^="imgSpr"],
[class*="imgSpr"] {{
    width: 24px;
    height: 24px;
}}

.dg_sport_icons_tinyest [class^="imgSpr"],
.dg_sport_icons_tinyest [class*="imgSpr"],
.tg_sport_icons_tinyest [class^="imgSpr"],
.tg_sport_icons_tinyest [class*="imgSpr"] {{
    width: 16px;
    height: 16px;
    background-size: 16px;
}}

.dg_sport_icons_tiny [class^="imgSpr"],
.dg_sport_icons_tiny [class*="imgSpr"],
.tg_sport_icons_tiny [class^="imgSpr"],
.tg_sport_icons_tiny [class*="imgSpr"] {{
    width: 20px;
    height: 20px;
    background-size: 20px;
}}

.sportIcons2x [class^="imgSpr"],
.sportIcons2x [class*="imgSpr"],
.dg_sport_icons_large [class^="imgSpr"],
.dg_sport_icons_large [class*="imgSpr"] {{
    width: 48px;
    height: 48px;
    background-size: 48px;
}}

/*============ 24 10 2022 ============*/
.dg_sport_icons_tinyest .imgSprDefault {{
    background-position: 0px -0px;
}}

.dg_sport_icons_tinyest .imgSpr0 {{
    background-position: 0px -16px;
}}

.dg_sport_icons_tinyest .imgSpr1 {{
    background-position: 0px -32px;
}}

.dg_sport_icons_tinyest .imgSpr2 {{
    background-position: 0px -48px;
}}

.dg_sport_icons_tinyest .imgSpr3 {{
    background-position: 0px -64px;
}}

.dg_sport_icons_tinyest .imgSpr4 {{
    background-position: 0px -80px;
}}

.dg_sport_icons_tinyest .imgSpr5 {{
    background-position: 0px -96px;
}}

.dg_sport_icons_tinyest .imgSpr6 {{
    background-position: 0px -112px;
}}

.dg_sport_icons_tinyest .imgSpr7 {{
    background-position: 0px -128px;
}}

.dg_sport_icons_tinyest .imgSpr8 {{
    background-position: 0px -144px;
}}

.dg_sport_icons_tinyest .imgSpr9 {{
    background-position: 0px -160px;
}}

.dg_sport_icons_tinyest .imgSpr10 {{
    background-position: 0px -176px;
}}

.dg_sport_icons_tinyest .imgSpr11 {{
    background-position: 0px -192px;
}}

.dg_sport_icons_tinyest .imgSpr12 {{
    background-position: 0px -208px;
}}

.dg_sport_icons_tinyest .imgSpr13 {{
    background-position: 0px -224px;
}}

.dg_sport_icons_tinyest .imgSpr14 {{
    background-position: 0px -240px;
}}

.dg_sport_icons_tinyest .imgSpr15 {{
    background-position: 0px -256px;
}}

.dg_sport_icons_tinyest .imgSpr16 {{
    background-position: 0px -272px;
}}

.dg_sport_icons_tinyest .imgSpr17 {{
    background-position: 0px -288px;
}}

.dg_sport_icons_tinyest .imgSpr18 {{
    background-position: 0px -304px;
}}

.dg_sport_icons_tinyest .imgSpr19 {{
    background-position: 0px -320px;
}}

.dg_sport_icons_tinyest .imgSpr20 {{
    background-position: 0px -336px;
}}

.dg_sport_icons_tinyest .imgSpr21 {{
    background-position: 0px -352px;
}}

.dg_sport_icons_tinyest .imgSpr22 {{
    background-position: 0px -368px;
}}

.dg_sport_icons_tinyest .imgSpr23 {{
    background-position: 0px -384px;
}}

.dg_sport_icons_tinyest .imgSpr24 {{
    background-position: 0px -400px;
}}

.dg_sport_icons_tinyest .imgSpr25 {{
    background-position: 0px -416px;
}}

.dg_sport_icons_tinyest .imgSpr26 {{
    background-position: 0px -432px;
}}

.dg_sport_icons_tinyest .imgSpr27 {{
    background-position: 0px -448px;
}}

.dg_sport_icons_tinyest .imgSpr28 {{
    background-position: 0px -464px;
}}

.dg_sport_icons_tinyest .imgSpr29 {{
    background-position: 0px -480px;
}}

.dg_sport_icons_tinyest .imgSpr30 {{
    background-position: 0px -496px;
}}

.dg_sport_icons_tinyest .imgSpr31 {{
    background-position: 0px -512px;
}}

.dg_sport_icons_tinyest .imgSpr32 {{
    background-position: 0px -528px;
}}

.dg_sport_icons_tinyest .imgSpr33 {{
    background-position: 0px -544px;
}}

.dg_sport_icons_tinyest .imgSpr34 {{
    background-position: 0px -560px;
}}

.dg_sport_icons_tinyest .imgSpr35 {{
    background-position: 0px -576px;
}}

.dg_sport_icons_tinyest .imgSpr36 {{
    background-position: 0px -592px;
}}

.dg_sport_icons_tinyest .imgSpr37 {{
    background-position: 0px -608px;
}}

.dg_sport_icons_tinyest .imgSpr38 {{
    background-position: 0px -624px;
}}

.dg_sport_icons_tinyest .imgSpr39 {{
    background-position: 0px -640px;
}}

.dg_sport_icons_tinyest .imgSpr40 {{
    background-position: 0px -656px;
}}

.dg_sport_icons_tinyest .imgSpr41 {{
    background-position: 0px -672px;
}}

.dg_sport_icons_tinyest .imgSpr42 {{
    background-position: 0px -688px;
}}

.dg_sport_icons_tinyest .imgSpr43 {{
    background-position: 0px -704px;
}}

.dg_sport_icons_tinyest .imgSpr44 {{
    background-position: 0px -720px;
}}

.dg_sport_icons_tinyest .imgSpr45 {{
    background-position: 0px -736px;
}}

.dg_sport_icons_tinyest .imgSpr46 {{
    background-position: 0px -752px;
}}

.dg_sport_icons_tinyest .imgSpr47 {{
    background-position: 0px -768px;
}}

.dg_sport_icons_tinyest .imgSpr48 {{
    background-position: 0px -784px;
}}

.dg_sport_icons_tinyest .imgSpr49 {{
    background-position: 0px -800px;
}}

.dg_sport_icons_tinyest .imgSpr50 {{
    background-position: 0px -816px;
}}

.dg_sport_icons_tinyest .imgSpr51 {{
    background-position: 0px -832px;
}}

.dg_sport_icons_tinyest .imgSpr52 {{
    background-position: 0px -848px;
}}

.dg_sport_icons_tinyest .imgSpr53 {{
    background-position: 0px -864px;
}}

.dg_sport_icons_tinyest .imgSpr54 {{
    background-position: 0px -880px;
}}

.dg_sport_icons_tinyest .imgSpr55 {{
    background-position: 0px -896px;
}}

.dg_sport_icons_tinyest .imgSpr56 {{
    background-position: 0px -912px;
}}

.dg_sport_icons_tinyest .imgSpr57 {{
    background-position: 0px -928px;
}}

.dg_sport_icons_tinyest .imgSpr58 {{
    background-position: 0px -944px;
}}

.dg_sport_icons_tinyest .imgSpr59 {{
    background-position: 0px -960px;
}}

.dg_sport_icons_tinyest .imgSpr60 {{
    background-position: 0px -976px;
}}

.dg_sport_icons_tinyest .imgSpr61 {{
    background-position: 0px -992px;
}}

.dg_sport_icons_tinyest .imgSpr62 {{
    background-position: 0px -1008px;
}}

.dg_sport_icons_tinyest .imgSpr63 {{
    background-position: 0px -1024px;
}}

.dg_sport_icons_tinyest .imgSpr64 {{
    background-position: 0px -1040px;
}}

.dg_sport_icons_tinyest .imgSpr65 {{
    background-position: 0px -1056px;
}}

.dg_sport_icons_tinyest .imgSpr66 {{
    background-position: 0px -1072px;
}}

.dg_sport_icons_tinyest .imgSpr67 {{
    background-position: 0px -1088px;
}}

.dg_sport_icons_tinyest .imgSpr68 {{
    background-position: 0px -1104px;
}}

.dg_sport_icons_tinyest .imgSpr69 {{
    background-position: 0px -1120px;
}}

.dg_sport_icons_tinyest .imgSpr70 {{
    background-position: 0px -1136px;
}}

.dg_sport_icons_tinyest .imgSpr71 {{
    background-position: 0px -1152px;
}}

.dg_sport_icons_tinyest .imgSpr72 {{
    background-position: 0px -1168px;
}}

.dg_sport_icons_tinyest .imgSpr73 {{
    background-position: 0px -1184px;
}}

.dg_sport_icons_tinyest .imgSpr74 {{
    background-position: 0px -1200px;
}}

.dg_sport_icons_tinyest .imgSpr75 {{
    background-position: 0px -1216px;
}}

.dg_sport_icons_tinyest .imgSpr76 {{
    background-position: 0px -1232px;
}}

.dg_sport_icons_tinyest .imgSpr77 {{
    background-position: 0px -1248px;
}}

.dg_sport_icons_tinyest .imgSpr78 {{
    background-position: 0px -1264px;
}}

.dg_sport_icons_tinyest .imgSpr79 {{
    background-position: 0px -1280px;
}}

.dg_sport_icons_tinyest .imgSpr80 {{
    background-position: 0px -1296px;
}}

.dg_sport_icons_tinyest .imgSpr81 {{
    background-position: 0px -1312px;
}}

.dg_sport_icons_tinyest .imgSpr82 {{
    background-position: 0px -1328px;
}}

.dg_sport_icons_tinyest .imgSpr83 {{
    background-position: 0px -1344px;
}}

.dg_sport_icons_tinyest .imgSpr84 {{
    background-position: 0px -1360px;
}}

.dg_sport_icons_tinyest .imgSpr85 {{
    background-position: 0px -1376px;
}}

.dg_sport_icons_tinyest .imgSpr86 {{
    background-position: 0px -1392px;
}}

.dg_sport_icons_tinyest .imgSpr87 {{
    background-position: 0px -1408px;
}}

.dg_sport_icons_tinyest .imgSpr88 {{
    background-position: 0px -1424px;
}}

.dg_sport_icons_tinyest .imgSpr89 {{
    background-position: 0px -1440px;
}}

.dg_sport_icons_tinyest .imgSpr90 {{
    background-position: 0px -1456px;
}}

.dg_sport_icons_tinyest .imgSpr91 {{
    background-position: 0px -1472px;
}}

.dg_sport_icons_tinyest .imgSpr92 {{
    background-position: 0px -1488px;
}}

.dg_sport_icons_tinyest .imgSpr93 {{
    background-position: 0px -1504px;
}}

.dg_sport_icons_tinyest .imgSpr94 {{
    background-position: 0px -1520px;
}}

.dg_sport_icons_tinyest .imgSpr95 {{
    background-position: 0px -1536px;
}}

.dg_sport_icons_tinyest .imgSpr96 {{
    background-position: 0px -1552px;
}}

.dg_sport_icons_tinyest .imgSpr97 {{
    background-position: 0px -1568px;
}}

.dg_sport_icons_tinyest .imgSpr98 {{
    background-position: 0px -1584px;
}}

.dg_sport_icons_tinyest .imgSpr99 {{
    background-position: 0px -1600px;
}}

.dg_sport_icons_tinyest .imgSpr100 {{
    background-position: 0px -1616px;
}}

.dg_sport_icons_tinyest .imgSpr101 {{
    background-position: 0px -1632px;
}}

.dg_sport_icons_tinyest .imgSpr102 {{
    background-position: 0px -1648px;
}}

.dg_sport_icons_tinyest .imgSpr103 {{
    background-position: 0px -1664px;
}}

.dg_sport_icons_tinyest .imgSpr104 {{
    background-position: 0px -1680px;
}}

.dg_sport_icons_tinyest .imgSpr105 {{
    background-position: 0px -1696px;
}}

.dg_sport_icons_tinyest .imgSpr106 {{
    background-position: 0px -1712px;
}}

.dg_sport_icons_tinyest .imgSpr107 {{
    background-position: 0px -1728px;
}}

.dg_sport_icons_tinyest .imgSpr108 {{
    background-position: 0px -1744px;
}}

.dg_sport_icons_tinyest .imgSpr109 {{
    background-position: 0px -1760px;
}}

.dg_sport_icons_tinyest .imgSpr110 {{
    background-position: 0px -1776px;
}}

.dg_sport_icons_tinyest .imgSpr111 {{
    background-position: 0px -1792px;
}}

.dg_sport_icons_tinyest .imgSpr112 {{
    background-position: 0px -1808px;
}}

.dg_sport_icons_tinyest .imgSpr113 {{
    background-position: 0px -1824px;
}}

.dg_sport_icons_tinyest .imgSpr116 {{
    background-position: 0px -1872px;
}}

.dg_sport_icons_tinyest .imgSpr117 {{
    background-position: 0px -1888px;
}}

.dg_sport_icons_tiny .imgSprDefault {{
    background-position: 0px -0px;
}}

.dg_sport_icons_tiny .imgSpr0 {{
    background-position: 0px -20px;
}}

.dg_sport_icons_tiny .imgSpr1 {{
    background-position: 0px -40px;
}}

.dg_sport_icons_tiny .imgSpr2 {{
    background-position: 0px -60px;
}}

.dg_sport_icons_tiny .imgSpr3 {{
    background-position: 0px -80px;
}}

.dg_sport_icons_tiny .imgSpr4 {{
    background-position: 0px -100px;
}}

.dg_sport_icons_tiny .imgSpr5 {{
    background-position: 0px -120px;
}}

.dg_sport_icons_tiny .imgSpr6 {{
    background-position: 0px -140px;
}}

.dg_sport_icons_tiny .imgSpr7 {{
    background-position: 0px -160px;
}}

.dg_sport_icons_tiny .imgSpr8 {{
    background-position: 0px -180px;
}}

.dg_sport_icons_tiny .imgSpr9 {{
    background-position: 0px -200px;
}}

.dg_sport_icons_tiny .imgSpr10 {{
    background-position: 0px -220px;
}}

.dg_sport_icons_tiny .imgSpr11 {{
    background-position: 0px -240px;
}}

.dg_sport_icons_tiny .imgSpr12 {{
    background-position: 0px -260px;
}}

.dg_sport_icons_tiny .imgSpr13 {{
    background-position: 0px -280px;
}}

.dg_sport_icons_tiny .imgSpr14 {{
    background-position: 0px -300px;
}}

.dg_sport_icons_tiny .imgSpr15 {{
    background-position: 0px -320px;
}}

.dg_sport_icons_tiny .imgSpr16 {{
    background-position: 0px -340px;
}}

.dg_sport_icons_tiny .imgSpr17 {{
    background-position: 0px -360px;
}}

.dg_sport_icons_tiny .imgSpr18 {{
    background-position: 0px -380px;
}}

.dg_sport_icons_tiny .imgSpr19 {{
    background-position: 0px -400px;
}}

.dg_sport_icons_tiny .imgSpr20 {{
    background-position: 0px -420px;
}}

.dg_sport_icons_tiny .imgSpr21 {{
    background-position: 0px -440px;
}}

.dg_sport_icons_tiny .imgSpr22 {{
    background-position: 0px -460px;
}}

.dg_sport_icons_tiny .imgSpr23 {{
    background-position: 0px -480px;
}}

.dg_sport_icons_tiny .imgSpr24 {{
    background-position: 0px -500px;
}}

.dg_sport_icons_tiny .imgSpr25 {{
    background-position: 0px -520px;
}}

.dg_sport_icons_tiny .imgSpr26 {{
    background-position: 0px -540px;
}}

.dg_sport_icons_tiny .imgSpr27 {{
    background-position: 0px -560px;
}}

.dg_sport_icons_tiny .imgSpr28 {{
    background-position: 0px -580px;
}}

.dg_sport_icons_tiny .imgSpr29 {{
    background-position: 0px -600px;
}}

.dg_sport_icons_tiny .imgSpr30 {{
    background-position: 0px -620px;
}}

.dg_sport_icons_tiny .imgSpr31 {{
    background-position: 0px -640px;
}}

.dg_sport_icons_tiny .imgSpr32 {{
    background-position: 0px -660px;
}}

.dg_sport_icons_tiny .imgSpr33 {{
    background-position: 0px -680px;
}}

.dg_sport_icons_tiny .imgSpr34 {{
    background-position: 0px -700px;
}}

.dg_sport_icons_tiny .imgSpr35 {{
    background-position: 0px -720px;
}}

.dg_sport_icons_tiny .imgSpr36 {{
    background-position: 0px -740px;
}}

.dg_sport_icons_tiny .imgSpr37 {{
    background-position: 0px -760px;
}}

.dg_sport_icons_tiny .imgSpr38 {{
    background-position: 0px -780px;
}}

.dg_sport_icons_tiny .imgSpr39 {{
    background-position: 0px -800px;
}}

.dg_sport_icons_tiny .imgSpr40 {{
    background-position: 0px -820px;
}}

.dg_sport_icons_tiny .imgSpr41 {{
    background-position: 0px -840px;
}}

.dg_sport_icons_tiny .imgSpr42 {{
    background-position: 0px -860px;
}}

.dg_sport_icons_tiny .imgSpr43 {{
    background-position: 0px -880px;
}}

.dg_sport_icons_tiny .imgSpr44 {{
    background-position: 0px -900px;
}}

.dg_sport_icons_tiny .imgSpr45 {{
    background-position: 0px -920px;
}}

.dg_sport_icons_tiny .imgSpr46 {{
    background-position: 0px -940px;
}}

.dg_sport_icons_tiny .imgSpr47 {{
    background-position: 0px -960px;
}}

.dg_sport_icons_tiny .imgSpr48 {{
    background-position: 0px -980px;
}}

.dg_sport_icons_tiny .imgSpr49 {{
    background-position: 0px -1000px;
}}

.dg_sport_icons_tiny .imgSpr50 {{
    background-position: 0px -1020px;
}}

.dg_sport_icons_tiny .imgSpr51 {{
    background-position: 0px -1040px;
}}

.dg_sport_icons_tiny .imgSpr52 {{
    background-position: 0px -1060px;
}}

.dg_sport_icons_tiny .imgSpr53 {{
    background-position: 0px -1080px;
}}

.dg_sport_icons_tiny .imgSpr54 {{
    background-position: 0px -1100px;
}}

.dg_sport_icons_tiny .imgSpr55 {{
    background-position: 0px -1120px;
}}

.dg_sport_icons_tiny .imgSpr56 {{
    background-position: 0px -1140px;
}}

.dg_sport_icons_tiny .imgSpr57 {{
    background-position: 0px -1160px;
}}

.dg_sport_icons_tiny .imgSpr58 {{
    background-position: 0px -1180px;
}}

.dg_sport_icons_tiny .imgSpr59 {{
    background-position: 0px -1200px;
}}

.dg_sport_icons_tiny .imgSpr60 {{
    background-position: 0px -1220px;
}}

.dg_sport_icons_tiny .imgSpr61 {{
    background-position: 0px -1240px;
}}

.dg_sport_icons_tiny .imgSpr62 {{
    background-position: 0px -1260px;
}}

.dg_sport_icons_tiny .imgSpr63 {{
    background-position: 0px -1280px;
}}

.dg_sport_icons_tiny .imgSpr64 {{
    background-position: 0px -1300px;
}}

.dg_sport_icons_tiny .imgSpr65 {{
    background-position: 0px -1320px;
}}

.dg_sport_icons_tiny .imgSpr66 {{
    background-position: 0px -1340px;
}}

.dg_sport_icons_tiny .imgSpr67 {{
    background-position: 0px -1360px;
}}

.dg_sport_icons_tiny .imgSpr68 {{
    background-position: 0px -1380px;
}}

.dg_sport_icons_tiny .imgSpr69 {{
    background-position: 0px -1400px;
}}

.dg_sport_icons_tiny .imgSpr70 {{
    background-position: 0px -1420px;
}}

.dg_sport_icons_tiny .imgSpr71 {{
    background-position: 0px -1440px;
}}

.dg_sport_icons_tiny .imgSpr72 {{
    background-position: 0px -1460px;
}}

.dg_sport_icons_tiny .imgSpr73 {{
    background-position: 0px -1480px;
}}

.dg_sport_icons_tiny .imgSpr74 {{
    background-position: 0px -1500px;
}}

.dg_sport_icons_tiny .imgSpr75 {{
    background-position: 0px -1520px;
}}

.dg_sport_icons_tiny .imgSpr76 {{
    background-position: 0px -1540px;
}}

.dg_sport_icons_tiny .imgSpr77 {{
    background-position: 0px -1560px;
}}

.dg_sport_icons_tiny .imgSpr78 {{
    background-position: 0px -1580px;
}}

.dg_sport_icons_tiny .imgSpr79 {{
    background-position: 0px -1600px;
}}

.dg_sport_icons_tiny .imgSpr80 {{
    background-position: 0px -1620px;
}}

.dg_sport_icons_tiny .imgSpr81 {{
    background-position: 0px -1640px;
}}

.dg_sport_icons_tiny .imgSpr82 {{
    background-position: 0px -1660px;
}}

.dg_sport_icons_tiny .imgSpr83 {{
    background-position: 0px -1680px;
}}

.dg_sport_icons_tiny .imgSpr84 {{
    background-position: 0px -1700px;
}}

.dg_sport_icons_tiny .imgSpr85 {{
    background-position: 0px -1720px;
}}

.dg_sport_icons_tiny .imgSpr86 {{
    background-position: 0px -1740px;
}}

.dg_sport_icons_tiny .imgSpr87 {{
    background-position: 0px -1760px;
}}

.dg_sport_icons_tiny .imgSpr88 {{
    background-position: 0px -1780px;
}}

.dg_sport_icons_tiny .imgSpr89 {{
    background-position: 0px -1800px;
}}

.dg_sport_icons_tiny .imgSpr90 {{
    background-position: 0px -1820px;
}}

.dg_sport_icons_tiny .imgSpr91 {{
    background-position: 0px -1840px;
}}

.dg_sport_icons_tiny .imgSpr92 {{
    background-position: 0px -1860px;
}}

.dg_sport_icons_tiny .imgSpr93 {{
    background-position: 0px -1880px;
}}

.dg_sport_icons_tiny .imgSpr94 {{
    background-position: 0px -1900px;
}}

.dg_sport_icons_tiny .imgSpr95 {{
    background-position: 0px -1920px;
}}

.dg_sport_icons_tiny .imgSpr96 {{
    background-position: 0px -1940px;
}}

.dg_sport_icons_tiny .imgSpr97 {{
    background-position: 0px -1960px;
}}

.dg_sport_icons_tiny .imgSpr98 {{
    background-position: 0px -1980px;
}}

.dg_sport_icons_tiny .imgSpr99 {{
    background-position: 0px -2000px;
}}

.dg_sport_icons_tiny .imgSpr100 {{
    background-position: 0px -2020px;
}}

.dg_sport_icons_tiny .imgSpr101 {{
    background-position: 0px -2040px;
}}

.dg_sport_icons_tiny .imgSpr102 {{
    background-position: 0px -2060px;
}}

.dg_sport_icons_tiny .imgSpr103 {{
    background-position: 0px -2080px;
}}

.dg_sport_icons_tiny .imgSpr104 {{
    background-position: 0px -2100px;
}}

.dg_sport_icons_tiny .imgSpr105 {{
    background-position: 0px -2120px;
}}

.dg_sport_icons_tiny .imgSpr106 {{
    background-position: 0px -2140px;
}}

.dg_sport_icons_tiny .imgSpr107 {{
    background-position: 0px -2160px;
}}

.dg_sport_icons_tiny .imgSpr108 {{
    background-position: 0px -2180px;
}}

.dg_sport_icons_tiny .imgSpr109 {{
    background-position: 0px -2200px;
}}

.dg_sport_icons_tiny .imgSpr110 {{
    background-position: 0px -2220px;
}}

.dg_sport_icons_tiny .imgSpr111 {{
    background-position: 0px -2240px;
}}

.dg_sport_icons_tiny .imgSpr112 {{
    background-position: 0px -2260px;
}}

.dg_sport_icons_tiny .imgSpr113 {{
    background-position: 0px -2280px;
}}

.dg_sport_icons_tiny .imgSpr116 {{
    background-position: 0px -2340px;
}}

.dg_sport_icons_tiny .imgSpr117 {{
    background-position: 0px -2360px;
}}

.imgSprDefault {{
    background-position: 0px -0px;
}}

.imgSpr0 {{
    background-position: 0px -24px;
}}

.imgSpr1 {{
    background-position: 0px -48px;
}}

.imgSpr2 {{
    background-position: 0px -72px;
}}

.imgSpr3 {{
    background-position: 0px -96px;
}}

.imgSpr4 {{
    background-position: 0px -120px;
}}

.imgSpr5 {{
    background-position: 0px -144px;
}}

.imgSpr6 {{
    background-position: 0px -168px;
}}

.imgSpr7 {{
    background-position: 0px -192px;
}}

.imgSpr8 {{
    background-position: 0px -216px;
}}

.imgSpr9 {{
    background-position: 0px -240px;
}}

.imgSpr10 {{
    background-position: 0px -264px;
}}

.imgSpr11 {{
    background-position: 0px -288px;
}}

.imgSpr12 {{
    background-position: 0px -312px;
}}

.imgSpr13 {{
    background-position: 0px -336px;
}}

.imgSpr14 {{
    background-position: 0px -360px;
}}

.imgSpr15 {{
    background-position: 0px -384px;
}}

.imgSpr16 {{
    background-position: 0px -408px;
}}

.imgSpr17 {{
    background-position: 0px -432px;
}}

.imgSpr18 {{
    background-position: 0px -456px;
}}

.imgSpr19 {{
    background-position: 0px -480px;
}}

.imgSpr20 {{
    background-position: 0px -504px;
}}

.imgSpr21 {{
    background-position: 0px -528px;
}}

.imgSpr22 {{
    background-position: 0px -552px;
}}

.imgSpr23 {{
    background-position: 0px -576px;
}}

.imgSpr24 {{
    background-position: 0px -600px;
}}

.imgSpr25 {{
    background-position: 0px -624px;
}}

.imgSpr26 {{
    background-position: 0px -648px;
}}

.imgSpr27 {{
    background-position: 0px -672px;
}}

.imgSpr28 {{
    background-position: 0px -696px;
}}

.imgSpr29 {{
    background-position: 0px -720px;
}}

.imgSpr30 {{
    background-position: 0px -744px;
}}

.imgSpr31 {{
    background-position: 0px -768px;
}}

.imgSpr32 {{
    background-position: 0px -792px;
}}

.imgSpr33 {{
    background-position: 0px -816px;
}}

.imgSpr34 {{
    background-position: 0px -840px;
}}

.imgSpr35 {{
    background-position: 0px -864px;
}}

.imgSpr36 {{
    background-position: 0px -888px;
}}

.imgSpr37 {{
    background-position: 0px -912px;
}}

.imgSpr38 {{
    background-position: 0px -936px;
}}

.imgSpr39 {{
    background-position: 0px -960px;
}}

.imgSpr40 {{
    background-position: 0px -984px;
}}

.imgSpr41 {{
    background-position: 0px -1008px;
}}

.imgSpr42 {{
    background-position: 0px -1032px;
}}

.imgSpr43 {{
    background-position: 0px -1056px;
}}

.imgSpr44 {{
    background-position: 0px -1080px;
}}

.imgSpr45 {{
    background-position: 0px -1104px;
}}

.imgSpr46 {{
    background-position: 0px -1128px;
}}

.imgSpr47 {{
    background-position: 0px -1152px;
}}

.imgSpr48 {{
    background-position: 0px -1176px;
}}

.imgSpr49 {{
    background-position: 0px -1200px;
}}

.imgSpr50 {{
    background-position: 0px -1224px;
}}

.imgSpr51 {{
    background-position: 0px -1248px;
}}

.imgSpr52 {{
    background-position: 0px -1272px;
}}

.imgSpr53 {{
    background-position: 0px -1296px;
}}

.imgSpr54 {{
    background-position: 0px -1320px;
}}

.imgSpr55 {{
    background-position: 0px -1344px;
}}

.imgSpr56 {{
    background-position: 0px -1368px;
}}

.imgSpr57 {{
    background-position: 0px -1392px;
}}

.imgSpr58 {{
    background-position: 0px -1416px;
}}

.imgSpr59 {{
    background-position: 0px -1440px;
}}

.imgSpr60 {{
    background-position: 0px -1464px;
}}

.imgSpr61 {{
    background-position: 0px -1488px;
}}

.imgSpr62 {{
    background-position: 0px -1512px;
}}

.imgSpr63 {{
    background-position: 0px -1536px;
}}

.imgSpr64 {{
    background-position: 0px -1560px;
}}

.imgSpr65 {{
    background-position: 0px -1584px;
}}

.imgSpr66 {{
    background-position: 0px -1608px;
}}

.imgSpr67 {{
    background-position: 0px -1632px;
}}

.imgSpr68 {{
    background-position: 0px -1656px;
}}

.imgSpr69 {{
    background-position: 0px -1680px;
}}

.imgSpr70 {{
    background-position: 0px -1704px;
}}

.imgSpr71 {{
    background-position: 0px -1728px;
}}

.imgSpr72 {{
    background-position: 0px -1752px;
}}

.imgSpr73 {{
    background-position: 0px -1776px;
}}

.imgSpr74 {{
    background-position: 0px -1800px;
}}

.imgSpr75 {{
    background-position: 0px -1824px;
}}

.imgSpr76 {{
    background-position: 0px -1848px;
}}

.imgSpr77 {{
    background-position: 0px -1872px;
}}

.imgSpr78 {{
    background-position: 0px -1896px;
}}

.imgSpr79 {{
    background-position: 0px -1920px;
}}

.imgSpr80 {{
    background-position: 0px -1944px;
}}

.imgSpr81 {{
    background-position: 0px -1968px;
}}

.imgSpr82 {{
    background-position: 0px -1992px;
}}

.imgSpr83 {{
    background-position: 0px -2016px;
}}

.imgSpr84 {{
    background-position: 0px -2040px;
}}

.imgSpr85 {{
    background-position: 0px -2064px;
}}

.imgSpr86 {{
    background-position: 0px -2088px;
}}

.imgSpr87 {{
    background-position: 0px -2112px;
}}

.imgSpr88 {{
    background-position: 0px -2136px;
}}

.imgSpr89 {{
    background-position: 0px -2160px;
}}

.imgSpr90 {{
    background-position: 0px -2184px;
}}

.imgSpr91 {{
    background-position: 0px -2208px;
}}

.imgSpr92 {{
    background-position: 0px -2232px;
}}

.imgSpr93 {{
    background-position: 0px -2256px;
}}

.imgSpr94 {{
    background-position: 0px -2280px;
}}

.imgSpr95 {{
    background-position: 0px -2304px;
}}

.imgSpr96 {{
    background-position: 0px -2328px;
}}

.imgSpr97 {{
    background-position: 0px -2352px;
}}

.imgSpr98 {{
    background-position: 0px -2376px;
}}

.imgSpr99 {{
    background-position: 0px -2400px;
}}

.imgSpr100 {{
    background-position: 0px -2424px;
}}

.imgSpr101 {{
    background-position: 0px -2448px;
}}

.imgSpr102 {{
    background-position: 0px -2472px;
}}

.imgSpr103 {{
    background-position: 0px -2496px;
}}

.imgSpr104 {{
    background-position: 0px -2520px;
}}

.imgSpr105 {{
    background-position: 0px -2544px;
}}

.imgSpr106 {{
    background-position: 0px -2568px;
}}

.imgSpr107 {{
    background-position: 0px -2592px;
}}

.imgSpr108 {{
    background-position: 0px -2616px;
}}

.imgSpr109 {{
    background-position: 0px -2640px;
}}

.imgSpr110 {{
    background-position: 0px -2664px;
}}

.imgSpr111 {{
    background-position: 0px -2688px;
}}

.imgSpr112 {{
    background-position: 0px -2712px;
}}

.imgSpr113 {{
    background-position: 0px -2736px;
}}

.imgSpr116 {{
    background-position: 0px -2808px;
}}

.imgSpr117 {{
    background-position: 0px -2832px;
}}

.dg_sport_icons_large .imgSprDefault {{
    background-position: 0px -0px;
}}

.dg_sport_icons_large .imgSpr0 {{
    background-position: 0px -48px;
}}

.dg_sport_icons_large .imgSpr1 {{
    background-position: 0px -96px;
}}

.dg_sport_icons_large .imgSpr2 {{
    background-position: 0px -144px;
}}

.dg_sport_icons_large .imgSpr3 {{
    background-position: 0px -192px;
}}

.dg_sport_icons_large .imgSpr4 {{
    background-position: 0px -240px;
}}

.dg_sport_icons_large .imgSpr5 {{
    background-position: 0px -288px;
}}

.dg_sport_icons_large .imgSpr6 {{
    background-position: 0px -336px;
}}

.dg_sport_icons_large .imgSpr7 {{
    background-position: 0px -384px;
}}

.dg_sport_icons_large .imgSpr8 {{
    background-position: 0px -432px;
}}

.dg_sport_icons_large .imgSpr9 {{
    background-position: 0px -480px;
}}

.dg_sport_icons_large .imgSpr10 {{
    background-position: 0px -528px;
}}

.dg_sport_icons_large .imgSpr11 {{
    background-position: 0px -576px;
}}

.dg_sport_icons_large .imgSpr12 {{
    background-position: 0px -624px;
}}

.dg_sport_icons_large .imgSpr13 {{
    background-position: 0px -672px;
}}

.dg_sport_icons_large .imgSpr14 {{
    background-position: 0px -720px;
}}

.dg_sport_icons_large .imgSpr15 {{
    background-position: 0px -768px;
}}

.dg_sport_icons_large .imgSpr16 {{
    background-position: 0px -816px;
}}

.dg_sport_icons_large .imgSpr17 {{
    background-position: 0px -864px;
}}

.dg_sport_icons_large .imgSpr18 {{
    background-position: 0px -912px;
}}

.dg_sport_icons_large .imgSpr19 {{
    background-position: 0px -960px;
}}

.dg_sport_icons_large .imgSpr20 {{
    background-position: 0px -1008px;
}}

.dg_sport_icons_large .imgSpr21 {{
    background-position: 0px -1056px;
}}

.dg_sport_icons_large .imgSpr22 {{
    background-position: 0px -1104px;
}}

.dg_sport_icons_large .imgSpr23 {{
    background-position: 0px -1152px;
}}

.dg_sport_icons_large .imgSpr24 {{
    background-position: 0px -1200px;
}}

.dg_sport_icons_large .imgSpr25 {{
    background-position: 0px -1248px;
}}

.dg_sport_icons_large .imgSpr26 {{
    background-position: 0px -1296px;
}}

.dg_sport_icons_large .imgSpr27 {{
    background-position: 0px -1344px;
}}

.dg_sport_icons_large .imgSpr28 {{
    background-position: 0px -1392px;
}}

.dg_sport_icons_large .imgSpr29 {{
    background-position: 0px -1440px;
}}

.dg_sport_icons_large .imgSpr30 {{
    background-position: 0px -1488px;
}}

.dg_sport_icons_large .imgSpr31 {{
    background-position: 0px -1536px;
}}

.dg_sport_icons_large .imgSpr32 {{
    background-position: 0px -1584px;
}}

.dg_sport_icons_large .imgSpr33 {{
    background-position: 0px -1632px;
}}

.dg_sport_icons_large .imgSpr34 {{
    background-position: 0px -1680px;
}}

.dg_sport_icons_large .imgSpr35 {{
    background-position: 0px -1728px;
}}

.dg_sport_icons_large .imgSpr36 {{
    background-position: 0px -1776px;
}}

.dg_sport_icons_large .imgSpr37 {{
    background-position: 0px -1824px;
}}

.dg_sport_icons_large .imgSpr38 {{
    background-position: 0px -1872px;
}}

.dg_sport_icons_large .imgSpr39 {{
    background-position: 0px -1920px;
}}

.dg_sport_icons_large .imgSpr40 {{
    background-position: 0px -1968px;
}}

.dg_sport_icons_large .imgSpr41 {{
    background-position: 0px -2016px;
}}

.dg_sport_icons_large .imgSpr42 {{
    background-position: 0px -2064px;
}}

.dg_sport_icons_large .imgSpr43 {{
    background-position: 0px -2112px;
}}

.dg_sport_icons_large .imgSpr44 {{
    background-position: 0px -2160px;
}}

.dg_sport_icons_large .imgSpr45 {{
    background-position: 0px -2208px;
}}

.dg_sport_icons_large .imgSpr46 {{
    background-position: 0px -2256px;
}}

.dg_sport_icons_large .imgSpr47 {{
    background-position: 0px -2304px;
}}

.dg_sport_icons_large .imgSpr48 {{
    background-position: 0px -2352px;
}}

.dg_sport_icons_large .imgSpr49 {{
    background-position: 0px -2400px;
}}

.dg_sport_icons_large .imgSpr50 {{
    background-position: 0px -2448px;
}}

.dg_sport_icons_large .imgSpr51 {{
    background-position: 0px -2496px;
}}

.dg_sport_icons_large .imgSpr52 {{
    background-position: 0px -2544px;
}}

.dg_sport_icons_large .imgSpr53 {{
    background-position: 0px -2592px;
}}

.dg_sport_icons_large .imgSpr54 {{
    background-position: 0px -2640px;
}}

.dg_sport_icons_large .imgSpr55 {{
    background-position: 0px -2688px;
}}

.dg_sport_icons_large .imgSpr56 {{
    background-position: 0px -2736px;
}}

.dg_sport_icons_large .imgSpr57 {{
    background-position: 0px -2784px;
}}

.dg_sport_icons_large .imgSpr58 {{
    background-position: 0px -2832px;
}}

.dg_sport_icons_large .imgSpr59 {{
    background-position: 0px -2880px;
}}

.dg_sport_icons_large .imgSpr60 {{
    background-position: 0px -2928px;
}}

.dg_sport_icons_large .imgSpr61 {{
    background-position: 0px -2976px;
}}

.dg_sport_icons_large .imgSpr62 {{
    background-position: 0px -3024px;
}}

.dg_sport_icons_large .imgSpr63 {{
    background-position: 0px -3072px;
}}

.dg_sport_icons_large .imgSpr64 {{
    background-position: 0px -3120px;
}}

.dg_sport_icons_large .imgSpr65 {{
    background-position: 0px -3168px;
}}

.dg_sport_icons_large .imgSpr66 {{
    background-position: 0px -3216px;
}}

.dg_sport_icons_large .imgSpr67 {{
    background-position: 0px -3264px;
}}

.dg_sport_icons_large .imgSpr68 {{
    background-position: 0px -3312px;
}}

.dg_sport_icons_large .imgSpr69 {{
    background-position: 0px -3360px;
}}

.dg_sport_icons_large .imgSpr70 {{
    background-position: 0px -3408px;
}}

.dg_sport_icons_large .imgSpr71 {{
    background-position: 0px -3456px;
}}

.dg_sport_icons_large .imgSpr72 {{
    background-position: 0px -3504px;
}}

.dg_sport_icons_large .imgSpr73 {{
    background-position: 0px -3552px;
}}

.dg_sport_icons_large .imgSpr74 {{
    background-position: 0px -3600px;
}}

.dg_sport_icons_large .imgSpr75 {{
    background-position: 0px -3648px;
}}

.dg_sport_icons_large .imgSpr76 {{
    background-position: 0px -3696px;
}}

.dg_sport_icons_large .imgSpr77 {{
    background-position: 0px -3744px;
}}

.dg_sport_icons_large .imgSpr78 {{
    background-position: 0px -3792px;
}}

.dg_sport_icons_large .imgSpr79 {{
    background-position: 0px -3840px;
}}

.dg_sport_icons_large .imgSpr80 {{
    background-position: 0px -3888px;
}}

.dg_sport_icons_large .imgSpr81 {{
    background-position: 0px -3936px;
}}

.dg_sport_icons_large .imgSpr82 {{
    background-position: 0px -3984px;
}}

.dg_sport_icons_large .imgSpr83 {{
    background-position: 0px -4032px;
}}

.dg_sport_icons_large .imgSpr84 {{
    background-position: 0px -4080px;
}}

.dg_sport_icons_large .imgSpr85 {{
    background-position: 0px -4128px;
}}

.dg_sport_icons_large .imgSpr86 {{
    background-position: 0px -4176px;
}}

.dg_sport_icons_large .imgSpr87 {{
    background-position: 0px -4224px;
}}

.dg_sport_icons_large .imgSpr88 {{
    background-position: 0px -4272px;
}}

.dg_sport_icons_large .imgSpr89 {{
    background-position: 0px -4320px;
}}

.dg_sport_icons_large .imgSpr90 {{
    background-position: 0px -4368px;
}}

.dg_sport_icons_large .imgSpr91 {{
    background-position: 0px -4416px;
}}

.dg_sport_icons_large .imgSpr92 {{
    background-position: 0px -4464px;
}}

.dg_sport_icons_large .imgSpr93 {{
    background-position: 0px -4512px;
}}

.dg_sport_icons_large .imgSpr94 {{
    background-position: 0px -4560px;
}}

.dg_sport_icons_large .imgSpr95 {{
    background-position: 0px -4608px;
}}

.dg_sport_icons_large .imgSpr96 {{
    background-position: 0px -4656px;
}}

.dg_sport_icons_large .imgSpr97 {{
    background-position: 0px -4704px;
}}

.dg_sport_icons_large .imgSpr98 {{
    background-position: 0px -4752px;
}}

.dg_sport_icons_large .imgSpr99 {{
    background-position: 0px -4800px;
}}

.dg_sport_icons_large .imgSpr100 {{
    background-position: 0px -4848px;
}}

.dg_sport_icons_large .imgSpr101 {{
    background-position: 0px -4896px;
}}

.dg_sport_icons_large .imgSpr102 {{
    background-position: 0px -4944px;
}}

.dg_sport_icons_large .imgSpr103 {{
    background-position: 0px -4992px;
}}

.dg_sport_icons_large .imgSpr104 {{
    background-position: 0px -5040px;
}}

.dg_sport_icons_large .imgSpr105 {{
    background-position: 0px -5088px;
}}

.dg_sport_icons_large .imgSpr106 {{
    background-position: 0px -5136px;
}}

.dg_sport_icons_large .imgSpr107 {{
    background-position: 0px -5184px;
}}

.dg_sport_icons_large .imgSpr108 {{
    background-position: 0px -5232px;
}}

.dg_sport_icons_large .imgSpr109 {{
    background-position: 0px -5280px;
}}

.dg_sport_icons_large .imgSpr110 {{
    background-position: 0px -5328px;
}}

.dg_sport_icons_large .imgSpr111 {{
    background-position: 0px -5376px;
}}

.dg_sport_icons_large .imgSpr112 {{
    background-position: 0px -5424px;
}}

.dg_sport_icons_large .imgSpr113 {{
    background-position: 0px -5472px;
}}

.dg_sport_icons_large .imgSpr116 {{
    background-position: 0px -5616px;
}}

.dg_sport_icons_large .imgSpr117 {{
    background-position: 0px -5664px;
}}

/*============ 24 10 2022 ============*/

@font-face {{
    font-family: "{FONT_FAMILY_NAME}";
    src: url("./{FONT_FILE_NAME}.eot?v{V}");
    src: url("./{FONT_FILE_NAME}.eot?#iefix&v{V}") format("embedded-opentype"),
         url("./{FONT_FILE_NAME}.woff2?v{V}") format("woff2"),
         url("./{FONT_FILE_NAME}.woff?v{V}") format("woff"),
         url("./{FONT_FILE_NAME}.ttf?v{V}") format("truetype");
    font-weight: 400;
    font-style: normal;
    font-display: block;
}}

.ico_size-xs{{
    --icoSize: 16px;
}}
.ico_size-sm{{
    --icoSize: 20px;
}}
.ico_size-md{{
    --icoSize: 24px;
}}
.ico_size-lg{{
    --icoSize: 28px;
}}
.ico_size-xl{{
    --icoSize: 32px;
}}

/*images or icons logick*/
.dg_sport_images [class^="imgSpr"]::before,
.dg_sport_images [class*="imgSpr"]::before {{
    content: "" !important;
}}

.dg_sport_icons [class^="imgSpr"],
.dg_sport_icons [class*="imgSpr"] {{
    background-image: none !important;
}}

.dg_tournament_images [class^="digi_tournament_"]:before,
.dg_tournament_images [class*="digi_tournament_"]:before {{
    content: "" !important;
}}

.dg_tournament_icon [class^="digi_tournament_"]:before,
.dg_tournament_icon [class*="digi_tournament_"]:before {{
    background-image: none !important;
}}

.dg_tournament_icon .sport_front_icon-82:before {{
    content: "\e051";
}}

/*----------------------------------------------*/

[class^="sport_front_icon-"],
[class*=" sport_front_icon-"] {{
    font-family: "digiSportIcons";
    display: inline-block;
    flex-shrink: 0;
    width: 24px;
    height: 24px;
    line-height: 23px;
    font-size: 35px;
    text-align: center;
    vertical-align: middle;
    font-weight: 400;
    font-style: normal;
    speak: none;
    text-decoration: inherit;
    text-transform: none;
    text-rendering: optimizeLegibility;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    content: "\e051";
    direction: ltr !important;
}}

.dg_sport_icons_tiny [class^="sport_front_icon-"],
.dg_sport_icons_tiny [class*=" sport_front_icon-"],
.tg_sport_icons_tiny [class^="sport_front_icon-"],
.tg_sport_icons_tiny [class*=" sport_front_icon-"] {{
    width: 20px;
    height: 20px;
    line-height: 19px;
    font-size: 29px;
}}

.dg_sport_icons_tinyest [class^="sport_front_icon-"],
.dg_sport_icons_tinyest [class*=" sport_front_icon-"],
.tg_sport_icons_tinyest [class^="sport_front_icon-"],
.tg_sport_icons_tinyest [class*=" sport_front_icon-"] {{
    width: 16px;
    height: 16px;
    line-height: 17px;
    font-size: 26px;
}}

[class^="sport_front_icon-"]:before,
[class*=" sport_front_icon-"]:before {{
    content: "\e051";
}}

/*RTL SUPPORT*/
.lv_rtl .sport_front_icon-arrow-left,
.dg_rtl .sport_front_icon-arrow-left {{
    content: "\e12b";
}}

.lv_rtl .sport_front_icon-arrow-right,
.dg_rtl .sport_front_icon-arrow-right {{
    content: "\e12a";
}}

/*
Glyphs list
*/

.sport_front_icon-1:before {{
    content: "\e0B7";
}}

.sport_front_icon-2:before {{
    content: "\e001";
}}

.sport_front_icon-3:before {{
    content: "\e002";
}}

.sport_front_icon-4:before {{
    content: "\e003";
}}

.sport_front_icon-5:before {{
    content: "\e004";
}}

.sport_front_icon-6:before {{
    content: "\e005";
}}

.sport_front_icon-7:before {{
    content: "\e006";
}}

.sport_front_icon-8:before {{
    content: "\e007";
}}

.sport_front_icon-9:before {{
    content: "\e008";
}}

.sport_front_icon-10:before {{
    content: "\e009";
}}

.sport_front_icon-11:before {{
    content: "\e00a";
}}

.sport_front_icon-12:before {{
    content: "\e00b";
}}

.sport_front_icon-13:before {{
    content: "\e00c";
}}

.sport_front_icon-14:before {{
    content: "\e00d";
}}

.sport_front_icon-15:before {{
    content: "\e00e";
}}

.sport_front_icon-16:before {{
    content: "\e00f";
}}

.sport_front_icon-17:before {{
    content: "\e010";
}}

.sport_front_icon-18:before {{
    content: "\e011";
}}

.sport_front_icon-19:before {{
    content: "\e012";
}}

.sport_front_icon-20:before {{
    content: "\e013";
}}

.sport_front_icon-21:before {{
    content: "\e014";
}}

.sport_front_icon-22:before {{
    content: "\e015";
}}

.sport_front_icon-23:before {{
    content: "\e016";
}}

.sport_front_icon-24:before {{
    content: "\e017";
}}

.sport_front_icon-25:before {{
    content: "\e018";
}}

.sport_front_icon-26:before {{
    content: "\e019";
}}

.sport_front_icon-27:before {{
    content: "\e01a";
}}

.sport_front_icon-28:before {{
    content: "\e01b";
}}

.sport_front_icon-29:before {{
    content: "\e01c";
}}

.sport_front_icon-30:before {{
    content: "\e01d";
}}

.sport_front_icon-31:before {{
    content: "\e01e";
}}

.sport_front_icon-32:before {{
    content: "\e01f";
}}

.sport_front_icon-33:before {{
    content: "\e020";
}}

.sport_front_icon-34:before {{
    content: "\e021";
}}

.sport_front_icon-35:before {{
    content: "\e022";
}}

.sport_front_icon-36:before {{
    content: "\e023";
}}

.sport_front_icon-37:before {{
    content: "\e024";
}}

.sport_front_icon-38:before {{
    content: "\e025";
}}

.sport_front_icon-39:before {{
    content: "\e026";
}}

.sport_front_icon-40:before {{
    content: "\e027";
}}

.sport_front_icon-41:before {{
    content: "\e028";
}}

.sport_front_icon-42:before {{
    content: "\e029";
}}

.sport_front_icon-43:before {{
    content: "\e02a";
}}

.sport_front_icon-44:before {{
    content: "\e02b";
}}

.sport_front_icon-45:before {{
    content: "\e02c";
}}

.sport_front_icon-46:before {{
    content: "\e02d";
}}

.sport_front_icon-47:before {{
    content: "\e02e";
}}

.sport_front_icon-48:before {{
    content: "\e02f";
}}

.sport_front_icon-49:before {{
    content: "\e030";
}}

.sport_front_icon-50:before {{
    content: "\e031";
}}

.sport_front_icon-51:before {{
    content: "\e032";
}}

.sport_front_icon-52:before {{
    content: "\e033";
}}

.sport_front_icon-53:before {{
    content: "\e034";
}}

.sport_front_icon-54:before {{
    content: "\e035";
}}

.sport_front_icon-55:before {{
    content: "\e036";
}}

.sport_front_icon-56:before {{
    content: "\e037";
}}

.sport_front_icon-57:before {{
    content: "\e038";
}}

.sport_front_icon-58:before {{
    content: "\e039";
}}

.sport_front_icon-59:before {{
    content: "\e03a";
}}

.sport_front_icon-60:before {{
    content: "\e03b";
}}

.sport_front_icon-61:before {{
    content: "\e03c";
}}

.sport_front_icon-62:before {{
    content: "\e03d";
}}

.sport_front_icon-63:before {{
    content: "\e03e";
}}

.sport_front_icon-64:before {{
    content: "\e03f";
}}

.sport_front_icon-65:before {{
    content: "\e040";
}}

.sport_front_icon-66:before {{
    content: "\e041";
}}

.sport_front_icon-67:before {{
    content: "\e042";
}}

.sport_front_icon-68:before {{
    content: "\e043";
}}

.sport_front_icon-69:before {{
    content: "\e044";
}}

.sport_front_icon-70:before {{
    content: "\e045";
}}

.sport_front_icon-71:before {{
    content: "\e046";
}}

.sport_front_icon-72:before {{
    content: "\e047";
}}

.sport_front_icon-73:before {{
    content: "\e048";
}}

.sport_front_icon-74:before {{
    content: "\e049";
}}

.sport_front_icon-75:before {{
    content: "\e04a";
}}

.sport_front_icon-76:before {{
    content: "\e04b";
}}

.sport_front_icon-77:before {{
    content: "\e04c";
}}

.sport_front_icon-78:before {{
    content: "\e04d";
}}

.sport_front_icon-79:before {{
    content: "\e04e";
}}

.sport_front_icon-80:before {{
    content: "\e04f";
}}

.sport_front_icon-81:before {{
    content: "\e050";
}}

.sport_front_icon-82:before {{
    content: "\e051";
}}

.sport_front_icon-83:before {{
    content: "\e052";
}}

.sport_front_icon-84:before {{
    content: "\e053";
}}

.sport_front_icon-85:before {{
    content: "\e054";
}}

.sport_front_icon-86:before {{
    content: "\e055";
}}

.sport_front_icon-87:before {{
    content: "\e056";
}}

.sport_front_icon-88:before {{
    content: "\e057";
}}

.sport_front_icon-89:before {{
    content: "\e058";
}}

.sport_front_icon-90:before {{
    content: "\e059";
}}

.sport_front_icon-91:before {{
    content: "\e05a";
}}

.sport_front_icon-92:before {{
    content: "\e05b";
}}

.sport_front_icon-93:before {{
    content: "\e05c";
}}

.sport_front_icon-94:before {{
    content: "\e05d";
}}

.sport_front_icon-95:before {{
    content: "\e05e";
}}

.sport_front_icon-96:before {{
    content: "\e05f";
}}

.sport_front_icon-97:before {{
    content: "\e060";
}}

.sport_front_icon-98:before {{
    content: "\e061";
}}

.sport_front_icon-99:before {{
    content: "\e062";
}}

.sport_front_icon-100:before {{
    content: "\e063";
}}

.sport_front_icon-101:before {{
    content: "\e064";
}}

.sport_front_icon-102:before {{
    content: "\e065";
}}

.sport_front_icon-103:before {{
    content: "\e066";
}}

.sport_front_icon-104:before {{
    content: "\e067";
}}

.sport_front_icon-105:before {{
    content: "\e068";
}}

.sport_front_icon-106:before {{
    content: "\e069";
}}

.sport_front_icon-107:before {{
    content: "\e06a";
}}

.sport_front_icon-108:before {{
    content: "\e06b";
}}

.sport_front_icon-109:before {{
    content: "\e06c";
}}

.sport_front_icon-110:before {{
    content: "\e06d";
}}

.sport_front_icon-111:before {{
    content: "\e06e";
}}

.sport_front_icon-112:before {{
    content: "\e06f";
}}

.sport_front_icon-113:before {{
    content: "\e070";
}}

.sport_front_icon-114:before {{
    content: "\e071";
}}

.sport_front_icon-115:before {{
    content: "\e072";
}}

.sport_front_icon-116:before {{
    content: "\e073";
}}

.sport_front_icon-117:before {{
    content: "\e074";
}}

/*other glyphs*/
.sport_front_icon-arrow-down:before {{
    content: "\e0b8";
}}

.sport_front_icon-arrow-up:before {{
    content: "\e0b9";
}}

.sport_front_icon-arrow-left:before {{
    content: "\e12a";
}}

.sport_front_icon-arrow-right:before {{
    content: "\e12b";
}}

.sport_front_icon-star-empty:before {{
    content: "\e0ba";
}}

.sport_front_icon-star-filled:before {{
    content: "\e0bb";
}}

.sport_front_icon-check:before {{
    content: "\e0bc";
}}

.sport_front_icon-search:before {{
    content: "\e0bd";
}}

.sport_front_icon-wallet:before {{
    content: "\e0be";
}}

.sport_front_icon-tournament:before {{
    content: "\e0bf";
}}

.sport_front_icon-sack:before {{
    content: "\e0c0";
}}

.sport_front_icon-bonus:before {{
    content: "\e0c1";
}}

.sport_front_icon-lock:before {{
    content: "\e0c2";
}}

.sport_front_icon-lock-off:before {{
    content: "\e0c3";
}}

.sport_front_icon-limit-top:before {{
    content: "\e0c4";
}}

.sport_front_icon-limit-bottom:before {{
    content: "\e0c5";
}}

.sport_front_icon-balance:before {{
    content: "\e0c6";
}}

.sport_front_icon-balance-negative:before {{
    content: "\e0c7";
}}

.sport_front_icon-copy:before {{
    content: "\e0c8";
}}

.sport_front_icon-dir-right:before {{
    content: "\e0c9";
}}

.sport_front_icon-dir-top:before {{
    content: "\e0cA";
}}

.sport_front_icon-logout:before {{
    content: "\e0cb";
}}

.sport_front_icon-cashier:before {{
    content: "\e0cc";
}}

.sport_front_icon-history:before {{
    content: "\e0cd";
}}

.sport_front_icon-offers:before {{
    content: "\e0ce";
}}

.sport_front_icon-settings:before {{
    content: "\e0cF";
}}

.sport_front_icon-documents:before {{
    content: "\e0d0";
}}

.sport_front_icon-key:before {{
    content: "\e0d1";
}}

.sport_front_icon-upload:before {{
    content: "\e0d2";
}}

.sport_front_icon-calendar-empty:before {{
    content: "\e0d3";
}}

.sport_front_icon-support:before {{
    content: "\e0d4";
}}

.sport_front_icon-promotions:before {{
    content: "\e0d5";
}}

.sport_front_icon-home:before {{
    content: "\e0d6";
}}

.sport_front_icon-sports:before {{
    content: "\e0d7";
}}

.sport_front_icon-live:before {{
    content: "\e0d8";
}}

.sport_front_icon-bet-checker:before {{
    content: "\e0d9";
}}

.sport_front_icon-live-score:before {{
    content: "\e0da";
}}

.sport_front_icon-statistics:before {{
    content: "\e0db";
}}

.sport_front_icon-results:before {{
    content: "\e0dc";
}}

.sport_front_icon-casino:before {{
    content: "\e0dd";
}}

.sport_front_icon-live-casino:before {{
    content: "\e0de";
}}

.sport_front_icon-rocketon:before {{
    content: "\e0df";
}}

.sport_front_icon-keno-express:before {{
    content: "\e0e0";
}}

.sport_front_icon-keno:before {{
    content: "\e0e1";
}}

.sport_front_icon-hilo:before {{
    content: "\e0e2";
}}

.sport_front_icon-sicBo:before {{
    content: "\e0e3";
}}

.sport_front_icon-blackJack:before {{
    content: "\e0e4";
}}

.sport_front_icon-crash:before {{
    content: "\e0e5";
}}

.sport_front_icon-penalty:before {{
    content: "\e0e6";
}}

.sport_front_icon-belote:before {{
    content: "\e0e7";
}}

.sport_front_icon-backgammon:before {{
    content: "\e0e8";
}}

.sport_front_icon-domino:before {{
    content: "\e0e9";
}}

.sport_front_icon-toto21:before {{
    content: "\e0ea";
}}

.sport_front_icon-baron:before {{
    content: "\e0eb";
}}

.sport_front_icon-rock-paper-scissors:before {{
    content: "\e0ec";
}}

.sport_front_icon-tv-games:before {{
    content: "\e0ed";
}}

.sport_front_icon-goal:before {{
    content: "\e0ee";
}}

.sport_front_icon-poker:before {{
    content: "\e0ef";
}}

.sport_front_icon-virtual-sport:before {{
    content: "\e0f0";
}}

.sport_front_icon-issue:before {{
    content: "\e0f1";
}}

.sport_front_icon-info:before {{
    content: "\e0f2";
}}

.sport_front_icon-calendar:before {{
    content: "\e0f3";
}}

.sport_front_icon-esports:before {{
    content: "\e034";
}}

.sport_front_icon-star-empty-modern:before {{
    content: "\e0f4";
}}

.sport_front_icon-star-filled-modern:before {{
    content: "\e0f5";
}}

.sport_front_icon-statistics-modern:before {{
    content: "\e0f6";
}}

.sport_front_icon-light-bulb:before {{
    content: "\e0f7";
}}

.sport_front_icon-live-stream:before {{
    content: "\e0f8";
}}

.sport_front_icon-bet-history:before {{
    content: "\e0f9" !important;
}}

.sport_front_icon-print:before {{
    content: "\e0fa";
}}

.sport_front_icon-boredraw:before {{
    content: "\e0fb";
}}

.sport_front_icon-cash-show:before {{
    content: "\e0fc";
}}

.sport_front_icon-cash-out:before {{
    content: "\e0fd";
}}

.sport_front_icon-plus:before {{
    content: "\e0fe";
}}

.sport_front_icon-minus:before {{
    content: "\e0ff";
}}

.sport_front_icon-checked:before {{
    content: "\e100";
}}

.sport_front_icon-bowl_modern:before {{
    content: "\e101";
}}

.sport_front_icon-filter_modern:before {{
    content: "\e102";
}}

.sport_front_icon-dots:before {{
    content: "\e103";
}}

.sport_front_icon-ask_davo:before {{
    content: "\e104";
}}

.sport_front_icon-wallet_modern:before {{
    content: "\e105";
}}

.sport_front_icon-bonus_modern:before {{
    content: "\e106";
}}

.sport_front_icon-repeat_bet:before {{
    content: "\e107";
}}

.sport_front_icon-check_redact:before {{
    content: "\e108";
}}

.sport_front_icon-share:before {{
    content: "\e109";
}}

.sport_front_icon-copy:before {{
    content: "\e10A";
}}

.sport_front_icon-calculator:before {{
    content: "\e10B";
}}

.sport_front_icon-burger:before {{
    content: "\e10C";
}}

.sport_front_icon-grid:before {{
    content: "\e10D";
}}

.sport_front_icon-group_stage:before {{
    content: "\e10E";
}}

.sport_front_icon-standings:before {{
    content: "\e10F";
}}

.sport_front_icon-statistics:before {{
    content: "\e110";
}}

.sport_front_icon-lucky_wheel:before {{
    content: "\e111";
}}

.sport_front_icon-bet_race:before {{
    content: "\e112";
}}

.sport_front_icon-bet_history:before {{
    content: "\e113";
}}

.sport_front_icon-results:before {{
    content: "\e114";
}}

.sport_front_icon-calendar_modern:before {{
    content: "\e115";
}}

.sport_front_icon-calendar_modern_2:before {{
    content: "\e116";
}}

.sport_front_icon-top_picks:before {{
    content: "\e11B";
}}

.sport_front_icon-cash__out:before {{
    content: "\e11C";
}}

.sport_front_icon-modern_info:before {{
    content: "\e11D";
}}

.sport_front_icon-modern_checked:before {{
    content: "\e11E";
}}

.sport_front_icon-modern_unchecked:before {{
    content: "\e11F";
}}

.sport_front_icon-circle_close:before {{
    content: "\e120";
}}

.sport_front_icon-close:before {{
    content: "\e121";
}}

.sport_front_icon-smart_pick:before {{
    content: "\e122";
}}

.sport_front_icon-tip:before {{
    content: "\e11a";
}}

.sport_front_icon-live:before {{
    content: "\e123";
}}

.sport_front_icon-upcoming:before {{
    content: "\e124";
}}

.sport_front_icon-user:before {{
    content: "\e119";
}}

.sport_front_icon-super:before {{
    content: "\e11a";
}}

.sport_front_icon-cashout_lt:before {{
    content: "\e126";
}}

.sport_front_icon-live_center:before {{
    content: "\e125";
}}

.sport_front_icon-colapse:before {{
    content: "\e12C";
}}

.sport_front_icon-arrow-up::before,
.sport_front_icon-arrow-down::before,
.sport_front_icon-arrow-left::before,
.sport_front_icon-arrow-right::before,
.sport_front_icon-colapse::before {{
    font-size: 42px;
}}

.sport_front_icon-top_picks_wc:before {{
    content: "\e12D";
}}

.sport_front_icon-ai:before {{
    content: "\e12F";
}}

.sport_front_icon-top_matches:before {{
    content: "\e12E";
}}

[class^="dg_icon_"],
[class*=" dg_icon_"] {{
    font-family: "digiSportIcons";
    display: inline-flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    width: 24px;
    height: 24px;
    line-height: 23px;
    font-size: 44px;
    font-weight: normal;
    font-style: normal;
    speak: none;
    text-decoration: inherit;
    text-transform: none;
    text-rendering: optimizeLegibility;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    content: "\e13f";
    direction: ltr !important;
}}

.dg_icon_xs {{
    width: 16px;
    height: 16px;
    line-height: 16px;
    font-size: 30px;
}}

/* This is checked */
.dg_icon_s {{
    width: 20px;
    height: 20px;
    line-height: 20px;
    font-size: 36px;
}}

.dg_icon_sport:before {{
    content: "\e13A";
}}

.dg_icon_star:before {{
    content: "\e13B";
}}

.dg_icon_star_filled:before {{
    content: "\e13C";
}}

.dg_icon_check:before {{
    content: "\e13D";
}}

.dg_icon_search:before {{
    content: "\e13E";
}}

.dg_icon_cup:before {{
    content: "\e13F";
}}

.dg_icon_bonus:before {{
    content: "\e140";
}}

.dg_icon_lock:before {{
    content: "\e141";
}}

.dg_icon_upload:before {{
    content: "\e142";
}}

.dg_icon_copy:before {{
    content: "\e143";
}}

.dg_icon_arrow_right:before {{
    content: "\e144";
}}

.dg_icon_arrow_down:before {{
    content: "\e145";
}}

.dg_icon_log_out:before {{
    content: "\e146";
}}

.dg_icon_bill:before {{
    content: "\e147";
}}

.dg_icon_download:before {{
    content: "\e148";
}}

.dg_icon_pie:before {{
    content: "\e149";
}}

.dg_icon_issue:before {{
    content: "\e14A";
}}

.dg_icon_info:before {{
    content: "\e14B";
}}

.dg_icon_download:before {{
    content: "\e148";
}}

.dg_icon_light_bulb:before {{
    content: "\e14C";
}}

.dg_icon_transfer:before {{
    content: "\e14D";
}}

.dg_icon_settings:before {{
    content: "\e14E";
}}

.dg_icon_document:before {{
    content: "\e14F";
}}

.dg_icon_key:before {{
    content: "\e150";
}}

.dg_icon_date_picker:before {{
    content: "\e151";
}}

.dg_icon_chat:before {{
    content: "\e152";
}}

.dg_icon_regulations:before {{
    content: "\e153";
}}

.dg_icon_home:before {{
    content: "\e154";
}}

.dg_icon_live:before {{
    content: "\e156";
}}

.dg_icon_bet_search:before {{
    content: "\e157";
}}

.dg_icon_stats:before {{
    content: "\e158";
}}

.dg_icon_burger:before {{
    content: "\e159";
}}

.dg_icon_card_view:before {{
    content: "\e15A";
}}

.dg_icon_list_view:before {{
    content: "\e15B";
}}

.dg_icon_standings:before {{
    content: "\e15C";
}}

.dg_icon_tv:before {{
    content: "\e15D";
}}

.dg_icon_plus_circular:before {{
    content: "\e160";
}}

.dg_icon_calculator:before {{
    content: "\e161";
}}

.dg_icon_lucky_wheel:before {{
    content: "\e162";
}}

.dg_icon_cash_out:before {{
    content: "\e163";
}}

.dg_icon_checkbox_circular_checked:before {{
    content: "\e164";
}}

.dg_icon_checkbox_circular:before {{
    content: "\e165";
}}

.dg_icon_angle_top:before {{
    content: "\e138";
}}

.dg_icon_angle_bottom:before {{
    content: "\e139";
}}

.dg_icon_angle_left:before {{
    content: "\e166";
}}

.dg_icon_angle_right:before {{
    content: "\e167";
}}

.dg_icon_angles_bottom:before {{
    content: "\e168";
}}

.dg_icon_worlds_cup:before {{
    content: "\e169";
}}

.dg_icon_top_matches:before {{
    content: "\e16A";
}}

.dg_icon_ai_widget:before {{
    content: "\e16B";
}}

.dg_icon_filter:before {{
    content: "\e16C";
}}

.dg_icon_more_vertical:before {{
    content: "\e16D";
}}

.dg_icon_auto_bet:before {{
    content: "\e16E";
}}

.dg_icon_repeat_bet:before {{
    content: "\e16F";
}}

.dg_icon_edit:before {{
    content: "\e170";
}}

.dg_icon_close_circular:before {{
    content: "\e171";
}}

.dg_icon_close:before {{
    content: "\e172";
}}

.dg_icon_smart_pick:before {{
    content: "\e173";
}}

.dg_icon_play_circular:before {{
    content: "\e174";
}}

.dg_icon_upcoming:before {{
    content: "\e175";
}}

.dg_icon_live_info:before {{
    content: "\e176";
}}

.dg_icon_checkbox_square_checked:before {{
    content: "\e177";
}}

.dg_icon_checkbox_square:before {{
    content: "\e178";
}}

.dg_icon_globe:before {{
    content: "\e179";
}}

.dg_icon_bet_race:before {{
    content: "\e17A";
}}

.dg_icon_bet_history:before {{
    content: "\e17B";
}}

.dg_icon_score_board:before {{
    content: "\e17C";
}}

.dg_icon_profile:before {{
    content: "\e17D";
}}

.dg_icon_offer_2x:before {{
    content: "\e132";
}}

.dg_icon_offer_2plus:before {{
    content: "\e133";
}}

.dg_icon_offer_00:before {{
    content: "\e134";
}}

.sport_front_icon-offer-x2:before {{
    content: "\e132";
}}

.sport_front_icon-badge-x2:before {{
    content: "\e133";
}}

.sport_front_icon-badge-00:before {{
    content: "\e134";
}}

.dg_icon_col_1:before {{
    content: "\e17E";
}}

.dg_icon_case:before {{
    content: "\e17F";
}}

.dg_icon_betslip:before {{
    content: "\e180";
}}

.dg_icon_uncheck_all:before {{
    content: "\e181";
}}

.dg_icon_check_all:before {{
    content: "\e182";
}}

.dg_icon_remove_all:before {{
    content: "\e183";
}}

.dg_icon_backspace:before {{
    content: "\e184";
}}

.dg_icon_link:before {{
    content: "\e185";
}}

.dg_icon_reload:before {{
    content: "\e186";
}}

.dg_icon_save:before {{
    content: "\e187";
}}

.dg_icon_remove_bet:before {{
    content: "\e188";
}}

.dg_icon_fb:before {{
    content: "\e189";
}}

.dg_icon_odno:before {{
    content: "\e18A";
}}

.dg_icon_vk:before {{
    content: "\e18B";
}}

.dg_icon_eye:before {{
    content: "\e18C";
}}

.dg_icon_eye_hide:before {{
    content: "\e18D";
}}

.dg_icon_double-arrow:before {{
    content: "\e18E";
}}

.dg_icon_pin:before {{
    content: "\e18f";
}}

.dg_icon_unpin:before {{
    content: "\e190";
}}

.dg_icon_hourglass:before {{
    content: "\e191";
}}




.dg_icon_market_swap:before {{
    content: "\e192";
}}

.dg_icon_offer_goals_ahead:before {{
    content: "\e193";
}}

.dg_icon_offer_default:before {{
    content: "\e194";
}}

/* .dg_icon_electro:before {{
    content: "\e195";
}} */

.dg_icon_odd_enhanced:before {{
    content: "\e195";
}}

.dg_icon_margin_null:before {{
    content: "\e196";
}}

.dg_icon_bet__builder::before {{
	content: "\e197";
}}

.dg_icon_cash__out_v2::before {{
	content: "\e198";
}}

.dg_icon_double__dooble::before {{
	content: "\e199";
}}

.dg_icon_edit__bet::before {{
	content: "\e19a";
}}

.dg_icon_my__bets::before {{
	content: "\e19b";
}}

"""
