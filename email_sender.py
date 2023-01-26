import smtplib, ssl
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_reset_email(rp_link, email):
    port = 587
    smtp_server = ''
    sender = ''
    user = ''
    recipient = email
    password = ''
    server = smtplib.SMTP(host = smtp_server,port= 587)
    server.starttls()
    server.login(user = user, password = password)
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "goHotel - Reset Password"
    msg['From'] = sender
    msg['To'] = recipient
    str = '''
      <body class="ic-1w42zm0" style="overflow: hidden">
      <style type="text/css" media="all">
        @media only screen and (max-width: 620px) {
          .span-2,
          .span-3 {
            max-width: none !important;
            width: 100% !important;
          }
          .span-2 > table,
          .span-3 > table {
            max-width: 100% !important;
            width: 100% !important;
          }
        }
        @media all {
          .btn-primary table td:hover {
            background-color: #3B82F6 !important;
          }
          .btn-primary a:hover {
            background-color: #3B82F6 !important;
            border-color: #3B82F6 !important;
          }
        }
        @media all {
          .btn-secondary a:hover {
            border-color: #34495e !important;
            color: #34495e !important;
          }
        }
        @media only screen and (max-width: 620px) {
          h1 {
            font-size: 28px !important;
            margin-bottom: 10px !important;
          }
          h2 {
            font-size: 22px !important;
            margin-bottom: 10px !important;
          }
          h3 {
            font-size: 16px !important;
            margin-bottom: 10px !important;
          }
          p,
          ul,
          ol,
          td,
          span,
          a {
            font-size: 16px !important;
          }
          .wrapper,
          .article {
            padding: 10px !important;
          }
          .content {
            padding: 0 !important;
          }
          .container {
            padding: 0 !important;
            width: 100% !important;
          }
          .header {
            margin-bottom: 10px !important;
          }
          .main {
            border-left-width: 0 !important;
            border-radius: 0 !important;
            border-right-width: 0 !important;
          }
          .btn table {
            width: 100% !important;
          }
          .btn a {
            width: 100% !important;
          }
          .img-responsive {
            height: auto !important;
            max-width: 100% !important;
            width: auto !important;
          }
          .alert td {
            border-radius: 0 !important;
            padding: 10px !important;
          }
          .receipt {
            width: 100% !important;
          }
        }

        @media all {
          .ExternalClass {
            width: 100%;
          }
          .ExternalClass,
          .ExternalClass p,
          .ExternalClass span,
          .ExternalClass font,
          .ExternalClass td,
          .ExternalClass div {
            line-height: 100%;
          }
          .apple-link a {
            color: inherit !important;
            font-family: inherit !important;
            font-size: inherit !important;
            font-weight: inherit !important;
            line-height: inherit !important;
            text-decoration: none !important;
          }
        }
      </style>

      <table
        bgcolor="#f6f6f6"
        width="100%"
        style="
          border-collapse: separate;
          mso-table-lspace: 0pt;
          mso-table-rspace: 0pt;
          width: 100%;
          background-color: #f6f6f6;
        "
        class="body"
        cellspacing="0"
        cellpadding="0"
        border="0"
      >
        <tbody>
          <tr>
            <td
              valign="top"
              style="
                font-family: sans-serif;
                font-size: 14px;
                vertical-align: top;
              "
            >
              &nbsp;
            </td>
            <td
              valign="top"
              width="580"
              style="
                font-family: sans-serif;
                font-size: 14px;
                vertical-align: top;
                margin: 0 auto !important;
                max-width: 580px;
                padding: 10px;
                width: 580px;
              "
              class="container"
            >
              <div
                style="
                  box-sizing: border-box;
                  display: block;
                  margin: 0 auto;
                  max-width: 580px;
                  padding: 10px;
                "
                class="content"
              >
                <div
                  style="margin-bottom: 20px; margin-top: 10px; width: 100%"
                  class="header"
                >
                  <table
                    width="100%"
                    style="
                      border-collapse: separate;
                      mso-table-lspace: 0pt;
                      mso-table-rspace: 0pt;
                      width: 100%;
                      min-width: 100%;
                    "
                    cellspacing="0"
                    cellpadding="0"
                    border="0"
                  >
                    <tbody>
                      <tr>
                        <td
                          align="center"
                          valign="top"
                          style="
                            font-family: sans-serif;
                            font-size: 14px;
                            vertical-align: top;
                            text-align: center;
                          "
                          class="align-center"
                        >
                          <img
                              style="
                                border: none;
                                -ms-interpolation-mode: bicubic;
                                max-width: 100%;
                              "
                              align="center"
                              alt="Logo"
                              width="120"
                              src="https://cdn.discordapp.com/attachments/659031245996556325/1043878238004449320/newlogo2.png"
                          />
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <table
                  width="100%"
                  style="
                    border-collapse: separate;
                    mso-table-lspace: 0pt;
                    mso-table-rspace: 0pt;
                    width: 100%;
                    background: #fff;
                    border-radius: 3px;
                  "
                  class="main"
                >
                  <tbody>
                    <tr>
                      <td
                        valign="top"
                        style="
                          font-family: sans-serif;
                          font-size: 14px;
                          vertical-align: top;
                          box-sizing: border-box;
                          padding: 20px;
                        "
                        class="wrapper"
                      >
                        <table
                          width="100%"
                          style="
                            border-collapse: separate;
                            mso-table-lspace: 0pt;
                            mso-table-rspace: 0pt;
                            width: 100%;
                          "
                          cellspacing="0"
                          cellpadding="0"
                          border="0"
                        >
                          <tbody>
                            <tr>
                              <td
                                valign="top"
                                style="
                                  font-family: sans-serif;
                                  font-size: 14px;
                                  vertical-align: top;
                                "
                              >
                                <h1
                                  style="
                                    color: #222222;
                                    font-family: sans-serif;
                                    font-weight: 300;
                                    line-height: 1.4;
                                    margin: 0;
                                    margin-bottom: 30px;
                                    font-size: 35px;
                                    text-align: center;
                                    text-transform: capitalize;
                                  "
                                >
                                  Password reset
                                </h1>
                                <p
                                  style="
                                    font-family: sans-serif;
                                    font-size: 14px;
                                    font-weight: normal;
                                    margin: 0;
                                    margin-bottom: 15px;
                                  "
                                >
                                  Seems like you forgot your password for
                                  goHotel. If this is true, click below to reset
                                  your password.
                                </p>
                                <table
                                  width="100%"
                                  style="
                                    border-collapse: separate;
                                    mso-table-lspace: 0pt;
                                    mso-table-rspace: 0pt;
                                    width: 100%;
                                    box-sizing: border-box;
                                    min-width: 100% !important;
                                  "
                                  class="btn btn-primary"
                                  cellspacing="0"
                                  cellpadding="0"
                                  border="0"
                                >
                                  <tbody>
                                    <tr>
                                      <td
                                        valign="top"
                                        style="
                                          font-family: sans-serif;
                                          font-size: 14px;
                                          vertical-align: top;
                                          padding-bottom: 15px;
                                        "
                                        align="center"
                                      >
                                        <table
                                          style="
                                            border-collapse: separate;
                                            mso-table-lspace: 0pt;
                                            mso-table-rspace: 0pt;
                                            width: auto;
                                          "
                                          cellspacing="0"
                                          cellpadding="0"
                                          border="0"
                                        >
                                          <tbody>
                                            <tr>
                                              <td
                                                align="center"
                                                bgcolor="#232E40"
                                                valign="top"
                                                style="
                                                  font-family: sans-serif;
                                                  font-size: 14px;
                                                  vertical-align: top;
                                                  background-color: #232E40;
                                                  border-radius: 5px;
                                                  text-align: center;
                                                "
                                              >
                                                <a
                                                  style="
                                                    display: inline-block;
                                                    color: #ffffff;
                                                    background-color: #232E40;
                                                    box-sizing: border-box;
                                                    cursor: pointer;
                                                    text-decoration: none;
                                                    font-size: 14px;
                                                    font-weight: bold;
                                                    margin: 0;
                                                    padding: 12px 25px;
                                                    text-transform: capitalize;
                                                    border-radius: 8px;
                                                  "
                                                  rel="noopener noreferrer"
                                                  href="rp_link"
                                                  >Reset my password</a
                                                >
                                              </td>
                                            </tr>
                                          </tbody>
                                        </table>
                                      </td>
                                    </tr>
                                  </tbody>
                                </table>
                                <p
                                  style="
                                    font-family: sans-serif;
                                    font-size: 14px;
                                    font-weight: normal;
                                    margin: 0;
                                    margin-bottom: 15px;
                                  "
                                >
                                  If you did not forget your password you can
                                  safely ignore this email.
                                </p>
                              </td>
                            </tr>
                            <tr height="20"></tr>
                            <tr>
                              <td>
                                <span style="
                                font-family: sans-serif;
                                font-size: 14px;
                              ">Press the button or </span><a
                                  style="
                                    font-family: sans-serif;
                                    font-size: 14px;
                                  "
                                  rel="noopener noreferrer"
                                  href="rp_link"
                                  >Click here</a
                                >
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </td>
                    </tr>
                  </tbody>
                </table>

                <div
                  style="
                    clear: both;
                    padding-top: 10px;
                    text-align: center;
                    width: 100%;
                  "
                  class="footer"
                >
                  <table
                    width="100%"
                    style="
                      border-collapse: separate;
                      mso-table-lspace: 0pt;
                      mso-table-rspace: 0pt;
                      width: 100%;
                    "
                    cellspacing="0"
                    cellpadding="0"
                    border="0"
                  >
                    <tbody>
                      <tr>
                        <td
                          align="center"
                          valign="top"
                          style="
                            font-family: sans-serif;
                            vertical-align: top;
                            padding-top: 10px;
                            padding-bottom: 10px;
                            font-size: 12px;
                            color: #999999;
                            text-align: center;
                          "
                          class="content-block"
                        >
                          <span
                            style="
                              color: #999999;
                              font-size: 12px;
                              text-align: center;
                            "
                            class="apple-link"
                            >goHotel is a service provided by lukxee.com</span
                          >
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </td>
            <td
              valign="top"
              style="
                font-family: sans-serif;
                font-size: 14px;
                vertical-align: top;
              "
            >
              &nbsp;
            </td>
          </tr>
        </tbody>
      </table>
      <img alt="" height="1px" width="1px" />
    </div>
  </body>
    '''
    html = str.replace('rp_link', rp_link)
    htmltext = MIMEText(html, 'html')
    msg.attach(htmltext)
    server.sendmail(sender, recipient, msg.as_string())
    server.quit()
    
    
def send_order_email(email, order_num, name, root_url, price, first_name, last_name, phone, house_num, address, city, county, postcode, residence, roomtype, checkin, checkout):
    #root_url = "http://localhost:5000/" # Since its not hosted to a domain it won't be able to find the root url, oops!
    port = 587
    smtp_server = ''
    sender = ''
    user = ''
    recipient = email
    password = ''
    server = smtplib.SMTP(host = smtp_server,port= 587)
    server.starttls()
    server.login(user = user, password = password)
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f"goHotel - ORDER #{order_num}"
    msg['From'] = sender
    msg['To'] = recipient
    str = '''
    <body class="ic-1w42zm0" style="">
    <div class="mail-message-defaults ic-1203xvo" style="margin: 0">
    <style>
      body {
        margin: 0;
      }
      h1 a:hover {
        font-size: 30px;
        color: #333;
      }
      h1 a:active {
        font-size: 30px;
        color: #333;
      }
      h1 a:visited {
        font-size: 30px;
        color: #333;
      }
      a:hover {
        text-decoration: none;
      }
      a:active {
        text-decoration: none;
      }
      a:visited {
        text-decoration: none;
      }
      .button__text:hover {
        color: #fff;
        text-decoration: none;
      }
      .button__text:active {
        color: #fff;
        text-decoration: none;
      }
      .button__text:visited {
        color: #fff;
        text-decoration: none;
      }
      a:hover {
        color: #000000;
      }
      a:active {
        color: #000000;
      }
      a:visited {
        color: #000000;
      }
      @media (max-width: 600px) {
        .container {
          width: 94% !important;
        }
        .main-action-cell {
          float: none !important;
          margin-right: 0 !important;
        }
        .secondary-action-cell {
          text-align: center;
          width: 100%;
        }
        .header {
          margin-top: 20px !important;
          margin-bottom: 2px !important;
        }
        .shop-name__cell {
          display: block;
        }
        .order-number__cell {
          display: block;
          text-align: left !important;
          margin-top: 20px;
        }
        .button {
          width: 100%;
        }
        .or {
          margin-right: 0 !important;
        }
        .apple-wallet-button {
          text-align: center;
        }
        .customer-info__item {
          display: block;
          width: 100% !important;
        }
        .spacer {
          display: none;
        }
        .subtotal-spacer {
          display: none;
        }
      }
    </style>

    <table
      style="
        height: 100% !important;
        width: 100% !important;
        border-spacing: 0;
        border-collapse: collapse;
      "
      class="body"
    >
      <tbody>
        <tr>
          <td
            style="
              font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI',
                'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans',
                'Droid Sans', 'Helvetica Neue', sans-serif;
            "
          >
            <table
              style="
                width: 100%;
                border-spacing: 0;
                border-collapse: collapse;
                margin: 40px 0 20px;
              "
              class="header row"
            >
              <tbody>
                <tr>
                  <td
                    style="
                      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI',
                        'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans',
                        'Droid Sans', 'Helvetica Neue', sans-serif;
                    "
                    class="header__cell"
                  >
                    <center>
                      <table
                        style="
                          width: 560px;
                          text-align: left;
                          border-spacing: 0;
                          border-collapse: collapse;
                          margin: 0 auto;
                        "
                        class="container"
                      >
                        <tbody>
                          <tr>
                            <td
                              style="
                                font-family: -apple-system, BlinkMacSystemFont,
                                  'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu',
                                  'Cantarell', 'Fira Sans', 'Droid Sans',
                                  'Helvetica Neue', sans-serif;
                              "
                            >
                              <table
                                style="
                                  width: 100%;
                                  border-spacing: 0;
                                  border-collapse: collapse;
                                "
                                class="row"
                              >
                                <tbody>
                                  <tr>
                                    <td
                                      style="
                                        font-family: -apple-system,
                                          BlinkMacSystemFont, 'Segoe UI',
                                          'Roboto', 'Oxygen', 'Ubuntu',
                                          'Cantarell', 'Fira Sans', 'Droid Sans',
                                          'Helvetica Neue', sans-serif;
                                      "
                                      class="shop-name__cell"
                                    >
                                      <img
                                        width="180"
                                        alt="logo"
                                        src="https://cdn.discordapp.com/attachments/659031245996556325/1043878238004449320/newlogo2.png"
                                      />
                                    </td>

                                    <td
                                      align="right"
                                      style="
                                        font-family: -apple-system,
                                          BlinkMacSystemFont, 'Segoe UI',
                                          'Roboto', 'Oxygen', 'Ubuntu',
                                          'Cantarell', 'Fira Sans', 'Droid Sans',
                                          'Helvetica Neue', sans-serif;
                                        text-transform: uppercase;
                                        font-size: 14px;
                                        color: #999;
                                      "
                                      class="order-number__cell"
                                    >
                                      <span
                                        style="font-size: 16px"
                                        class="order-number__text"
                                      >
                                        Order #{order_num}
                                      </span>
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </center>
                  </td>
                </tr>
              </tbody>
            </table>

            <table
              style="width: 100%; border-spacing: 0; border-collapse: collapse"
              class="row content"
            >
              <tbody>
                <tr>
                  <td
                    style="
                      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI',
                        'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans',
                        'Droid Sans', 'Helvetica Neue', sans-serif;
                      padding-bottom: 40px;
                      border: 0;
                    "
                    class="content__cell"
                  >
                    <center>
                      <table
                        style="
                          width: 560px;
                          text-align: left;
                          border-spacing: 0;
                          border-collapse: collapse;
                          margin: 0 auto;
                        "
                        class="container"
                      >
                        <tbody>
                          <tr>
                            <td
                              style="
                                font-family: -apple-system, BlinkMacSystemFont,
                                  'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu',
                                  'Cantarell', 'Fira Sans', 'Droid Sans',
                                  'Helvetica Neue', sans-serif;
                              "
                            >
                              <h2
                                style="
                                  font-weight: normal;
                                  font-size: 24px;
                                  margin: 0 0 10px;
                                "
                              >
                                Thank you for your order!
                              </h2>
                              <p
                                style="
                                  color: #777;
                                  line-height: 150%;
                                  font-size: 16px;
                                  margin: 0;
                                "
                              >
                                Hi {name}, thanks for your order! Please go ahead and make sure all your details are correct below. If you have any questions, please don't hesitate to contact us at <a
                                style="
                                  text-decoration: none;
                                  color: #000000;
                                "
                                href="mailto:nea@lukxee.com"
                                >nea@lukxee.com</a
                              >. <br><br>
                              When picking up your key there will be a self service checkin at the reception where you can enter your order number to have your key printed 24/7, or you can ask the receptionist to print it for you at the receptionist desk.
                              </p>

                              <table
                                style="
                                  width: 100%;
                                  border-spacing: 0;
                                  border-collapse: collapse;
                                  margin-top: 20px;
                                "
                                class="row actions"
                              >
                                <tbody>
                                  <tr>
                                    <td
                                      style="
                                        font-family: -apple-system,
                                          BlinkMacSystemFont, 'Segoe UI',
                                          'Roboto', 'Oxygen', 'Ubuntu',
                                          'Cantarell', 'Fira Sans', 'Droid Sans',
                                          'Helvetica Neue', sans-serif;
                                        line-height: 0em;
                                      "
                                      class="empty-line"
                                    >
                                      &nbsp;
                                    </td>
                                  </tr>
                                  <tr>
                                    <td
                                      style="
                                        font-family: -apple-system,
                                          BlinkMacSystemFont, 'Segoe UI',
                                          'Roboto', 'Oxygen', 'Ubuntu',
                                          'Cantarell', 'Fira Sans', 'Droid Sans',
                                          'Helvetica Neue', sans-serif;
                                      "
                                      class="actions__cell"
                                    >
                                      <table
                                        style="
                                          border-spacing: 0;
                                          border-collapse: collapse;
                                          float: left;
                                          margin-right: 15px;
                                        "
                                        class="button main-action-cell"
                                      >
                                        <tbody>
                                          <tr>
                                            <td
                                              bgcolor="#232E40"
                                              align="center"
                                              style="
                                                font-family: -apple-system,
                                                  BlinkMacSystemFont, 'Segoe UI',
                                                  'Roboto', 'Oxygen', 'Ubuntu',
                                                  'Cantarell', 'Fira Sans',
                                                  'Droid Sans', 'Helvetica Neue',
                                                  sans-serif;
                                                border-radius: 5px;
                                              "
                                              class="button__cell"
                                            >
                                              <a
                                                style="
                                                  text-decoration: none;
                                                  display: block;
                                                  color: #fff;
                                                  font-size: 14px;
                                                  font-weight: bold;
                                                  margin: 0;
                                                  padding: 12px 25px;
                                                "
                                                class="button__text"
                                                rel="noopener noreferrer"
                                                href="{root_url}"
                                                >Visit our site</a
                                              >
                                            </td>
                                          </tr>
                                        </tbody>
                                      </table>

                                      <table
                                        style="
                                          border-spacing: 0;
                                          border-collapse: collapse;
                                          margin-top: 19px;
                                        "
                                        class="link secondary-action-cell"
                                      >
                                        <tbody>
                                          <!--<tr>
                                            <td
                                              style="
                                                font-family: -apple-system,
                                                  BlinkMacSystemFont, 'Segoe UI',
                                                  'Roboto', 'Oxygen', 'Ubuntu',
                                                  'Cantarell', 'Fira Sans',
                                                  'Droid Sans', 'Helvetica Neue',
                                                  sans-serif;
                                              "
                                              class="link__cell"
                                            >
                                              or
                                              <a
                                                style="
                                                  font-size: 16px;
                                                  text-decoration: none;
                                                  color: #000000;
                                                "
                                                rel="noopener noreferrer"
                                                href="{root_url}"
                                                >Visit our site</a
                                              >
                                            </td>
                                          </tr>-->
                                        </tbody>
                                      </table>
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </center>
                  </td>
                </tr>
              </tbody>
            </table>

            <table
              style="width: 100%; border-spacing: 0; border-collapse: collapse"
              class="row section"
            >
              <tbody>
                <tr>
                  <td
                    style="
                      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI',
                        'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans',
                        'Droid Sans', 'Helvetica Neue', sans-serif;
                      padding: 40px 0;
                    "
                    class="section__cell"
                  >
                    <center>
                      <table
                        style="
                          width: 560px;
                          text-align: left;
                          border-spacing: 0;
                          border-collapse: collapse;
                          margin: 0 auto;
                        "
                        class="container"
                      >
                        <tbody>
                          <tr>
                            <td
                              style="
                                font-family: -apple-system, BlinkMacSystemFont,
                                  'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu',
                                  'Cantarell', 'Fira Sans', 'Droid Sans',
                                  'Helvetica Neue', sans-serif;
                              "
                            >
                              <h3
                                style="
                                  font-weight: normal;
                                  font-size: 20px;
                                  margin: 0 0 25px;
                                "
                              >
                                Order summary
                              </h3>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                      <table
                        style="
                          width: 560px;
                          text-align: left;
                          border-spacing: 0;
                          border-collapse: collapse;
                          margin: 0 auto;
                        "
                        class="container"
                      >
                        <tbody>
                          <tr>
                            <td
                              style="
                                font-family: -apple-system, BlinkMacSystemFont,
                                  'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu',
                                  'Cantarell', 'Fira Sans', 'Droid Sans',
                                  'Helvetica Neue', sans-serif;
                              "
                            >
                              <table
                                style="
                                  width: 100%;
                                  border-spacing: 0;
                                  border-collapse: collapse;
                                "
                                class="row"
                              >
                                <tbody>
                                  <tr
                                    style="width: 100%"
                                    class="order-list__item"
                                  >
                                    <td
                                      style="
                                        font-family: -apple-system,
                                          BlinkMacSystemFont, 'Segoe UI',
                                          'Roboto', 'Oxygen', 'Ubuntu',
                                          'Cantarell', 'Fira Sans', 'Droid Sans',
                                          'Helvetica Neue', sans-serif;
                                        padding-bottom: 15px;
                                      "
                                      class="order-list__item__cell"
                                    >
                                      <table
                                        style="
                                          border-spacing: 0;
                                          border-collapse: collapse;
                                        "
                                      >
                                        <tbody>
                                          <tr>
                                            <td
                                              style="
                                                font-family: -apple-system,
                                                  BlinkMacSystemFont, 'Segoe UI',
                                                  'Roboto', 'Oxygen', 'Ubuntu',
                                                  'Cantarell', 'Fira Sans',
                                                  'Droid Sans', 'Helvetica Neue',
                                                  sans-serif;
                                              "
                                            >
                                              <img
                                                style="
                                                  margin-right: 15px;
                                                  border-radius: 8px;
                                                  border: 1px solid #e5e5e5;
                                                "
                                                class="order-list__product-image"
                                                height="60"
                                                width="60"
                                                align="left"
                                                src="https://cdn.discordapp.com/attachments/712721429866741900/1046522561586008174/hotel-room.png"
                                              />
                                            </td>
                                            <td
                                              style="
                                                font-family: -apple-system,
                                                  BlinkMacSystemFont, 'Segoe UI',
                                                  'Roboto', 'Oxygen', 'Ubuntu',
                                                  'Cantarell', 'Fira Sans',
                                                  'Droid Sans', 'Helvetica Neue',
                                                  sans-serif;
                                                width: 100%;
                                              "
                                              class="order-list__product-description-cell"
                                            >
                                              <span
                                                style="
                                                  font-size: 16px;
                                                  font-weight: 600;
                                                  line-height: 1.4;
                                                  color: #555;
                                                "
                                                class="order-list__item-title"
                                                >Room</span
                                              ><br />

                                              <span
                                                style="
                                                  font-size: 14px;
                                                  color: #999;
                                                "
                                                class="order-list__item-variant"
                                                >{type}<br>
                                                {checkin} - {checkout}</span
                                              ><br />
                                            </td>
                                            <td
                                              style="
                                                font-family: -apple-system,
                                                  BlinkMacSystemFont, 'Segoe UI',
                                                  'Roboto', 'Oxygen', 'Ubuntu',
                                                  'Cantarell', 'Fira Sans',
                                                  'Droid Sans', 'Helvetica Neue',
                                                  sans-serif;
                                                white-space: nowrap;
                                              "
                                              class="order-list__price-cell"
                                            
                                              >

                                              <p
                                                align="right"
                                                style="
                                                  color: #555;
                                                  line-height: 150%;
                                                  font-size: 16px;
                                                  font-weight: 600;
                                                  margin: 0 0 0 15px;
                                                "
                                                class="order-list__item-price"
                                              >
                                                {price}
                                              </p>
                                            </td>
                                          </tr>
                                        </tbody>
                                      </table>
                                    </td>
                                  </tr>
                                  <tr
                                    style="
                                      width: 100%;
                                      border-top-width: 1px;
                                      border-top-color: #e5e5e5;
                                      border-top-style: solid;
                                    "
                                    class="order-list__item"
                                  >
                                    <td
                                      style="
                                        font-family: -apple-system,
                                          BlinkMacSystemFont, 'Segoe UI',
                                          'Roboto', 'Oxygen', 'Ubuntu',
                                          'Cantarell', 'Fira Sans', 'Droid Sans',
                                          'Helvetica Neue', sans-serif;
                                        padding-top: 15px;
                                      "
                                      class="order-list__item__cell"
                                    >
                                      <table
                                        style="
                                          border-spacing: 0;
                                          border-collapse: collapse;
                                        "
                                      >
                                        <tbody>
                                          <tr>
                                            <td
                                              style="
                                                font-family: -apple-system,
                                                  BlinkMacSystemFont, 'Segoe UI',
                                                  'Roboto', 'Oxygen', 'Ubuntu',
                                                  'Cantarell', 'Fira Sans',
                                                  'Droid Sans', 'Helvetica Neue',
                                                  sans-serif;
                                              "
                                            >
                                              <img
                                                style="
                                                  margin-right: 15px;
                                                  border-radius: 8px;
                                                  border: 1px solid #e5e5e5;
                                                "
                                                class="order-list__product-image"
                                                height="60"
                                                width="60"
                                                align="left"
                                                src="https://cdn.discordapp.com/attachments/712721429866741900/1046523734556688494/services.png"
                                              />
                                            </td>
                                            <td
                                              style="
                                                font-family: -apple-system,
                                                  BlinkMacSystemFont, 'Segoe UI',
                                                  'Roboto', 'Oxygen', 'Ubuntu',
                                                  'Cantarell', 'Fira Sans',
                                                  'Droid Sans', 'Helvetica Neue',
                                                  sans-serif;
                                                width: 100%;
                                              "
                                              class="order-list__product-description-cell"
                                            >
                                              <span
                                                style="
                                                  font-size: 16px;
                                                  font-weight: 600;
                                                  line-height: 1.4;
                                                  color: #555;
                                                "
                                                class="order-list__item-title"
                                                >Services</span
                                              ><br />

                                              <span
                                                style="
                                                  font-size: 14px;
                                                  color: #999;
                                                "
                                                class="order-list__item-variant"
                                                >Housekeeping<br>
                                                Breakfast & Dinner<br>
                                                Air Conditioning<br>
                                                Swimming<br>
                                                Wifi</span
                                              ><br />
                                            </td>
                                            <td
                                              style="
                                                font-family: -apple-system,
                                                  BlinkMacSystemFont, 'Segoe UI',
                                                  'Roboto', 'Oxygen', 'Ubuntu',
                                                  'Cantarell', 'Fira Sans',
                                                  'Droid Sans', 'Helvetica Neue',
                                                  sans-serif;
                                                white-space: nowrap;
                                              "
                                              class="order-list__price-cell"
                                            >
                                              <p
                                                align="right"
                                                style="
                                                  color: #555;
                                                  line-height: 150%;
                                                  font-size: 16px;
                                                  font-weight: 600;
                                                  margin: 0 0 0 15px;
                                                "
                                                class="order-list__item-price"
                                              >
                                                Free
                                              </p>
                                            </td>
                                          </tr>
                                        </tbody>
                                      </table>
                                    </td>
                                  </tr>
                                </tbody>
                              </table>

                              <table
                                style="
                                  width: 100%;
                                  border-spacing: 0;
                                  border-collapse: collapse;
                                  margin-top: 15px;
                                  border-top-width: 1px;
                                  border-top-color: #e5e5e5;
                                  border-top-style: solid;
                                "
                                class="row subtotal-lines"
                              >
                                <tbody>
                                  <tr>
                                    <td
                                      style="
                                        font-family: -apple-system,
                                          BlinkMacSystemFont, 'Segoe UI',
                                          'Roboto', 'Oxygen', 'Ubuntu',
                                          'Cantarell', 'Fira Sans', 'Droid Sans',
                                          'Helvetica Neue', sans-serif;
                                        width: 40%;
                                      "
                                      class="subtotal-spacer"
                                    ></td>
                                    <td
                                      style="
                                        font-family: -apple-system,
                                          BlinkMacSystemFont, 'Segoe UI',
                                          'Roboto', 'Oxygen', 'Ubuntu',
                                          'Cantarell', 'Fira Sans', 'Droid Sans',
                                          'Helvetica Neue', sans-serif;
                                      "
                                    >
                                      <table
                                        style="
                                          width: 100%;
                                          border-spacing: 0;
                                          border-collapse: collapse;
                                          margin-top: 20px;
                                        "
                                        class="row subtotal-table"
                                      >
                                        <tbody>
                                          <tr class="subtotal-line">
                                            <td
                                              style="
                                                font-family: -apple-system,
                                                  BlinkMacSystemFont, 'Segoe UI',
                                                  'Roboto', 'Oxygen', 'Ubuntu',
                                                  'Cantarell', 'Fira Sans',
                                                  'Droid Sans', 'Helvetica Neue',
                                                  sans-serif;
                                                padding: 5px 0;
                                              "
                                              class="subtotal-line__title"
                                            >
                                              <p
                                                style="
                                                  color: #777;
                                                  line-height: 1.2em;
                                                  font-size: 16px;
                                                  margin: 0;
                                                "
                                              >
                                                <span style="font-size: 16px"
                                                  >Subtotal</span
                                                >
                                              </p>
                                            </td>
                                            <td
                                              align="right"
                                              style="
                                                font-family: -apple-system,
                                                  BlinkMacSystemFont, 'Segoe UI',
                                                  'Roboto', 'Oxygen', 'Ubuntu',
                                                  'Cantarell', 'Fira Sans',
                                                  'Droid Sans', 'Helvetica Neue',
                                                  sans-serif;
                                                padding: 5px 0;
                                              "
                                              class="subtotal-line__value"
                                            >
                                              <strong
                                                style="
                                                  font-size: 16px;
                                                  color: #555;
                                                "
                                                >{price}</strong
                                              >
                                            </td>
                                          </tr>

                                          <tr class="subtotal-line">
                                            <td
                                              style="
                                                font-family: -apple-system,
                                                  BlinkMacSystemFont, 'Segoe UI',
                                                  'Roboto', 'Oxygen', 'Ubuntu',
                                                  'Cantarell', 'Fira Sans',
                                                  'Droid Sans', 'Helvetica Neue',
                                                  sans-serif;
                                                padding: 5px 0;
                                              "
                                              class="subtotal-line__title"
                                            >
                                            </td>
                                            <td
                                              align="right"
                                              style="
                                                font-family: -apple-system,
                                                  BlinkMacSystemFont, 'Segoe UI',
                                                  'Roboto', 'Oxygen', 'Ubuntu',
                                                  'Cantarell', 'Fira Sans',
                                                  'Droid Sans', 'Helvetica Neue',
                                                  sans-serif;
                                                padding: 5px 0;
                                              "
                                              class="subtotal-line__value"
                                            >
                                            </td>
                                          </tr>

                                          <tr class="subtotal-line">
                                            <td
                                              style="
                                                font-family: -apple-system,
                                                  BlinkMacSystemFont, 'Segoe UI',
                                                  'Roboto', 'Oxygen', 'Ubuntu',
                                                  'Cantarell', 'Fira Sans',
                                                  'Droid Sans', 'Helvetica Neue',
                                                  sans-serif;
                                                padding: 5px 0;
                                              "
                                              class="subtotal-line__title"
                                            >
                                              <p
                                                style="
                                                  color: #777;
                                                  line-height: 1.2em;
                                                  font-size: 16px;
                                                  margin: 0;
                                                "
                                              >
                                                <span style="font-size: 16px"
                                                  >Taxes</span
                                                >
                                              </p>
                                            </td>
                                            <td
                                              align="right"
                                              style="
                                                font-family: -apple-system,
                                                  BlinkMacSystemFont, 'Segoe UI',
                                                  'Roboto', 'Oxygen', 'Ubuntu',
                                                  'Cantarell', 'Fira Sans',
                                                  'Droid Sans', 'Helvetica Neue',
                                                  sans-serif;
                                                padding: 5px 0;
                                              "
                                              class="subtotal-line__value"
                                            >
                                              <strong
                                                style="
                                                  font-size: 16px;
                                                  color: #555;
                                                "
                                                >0.00</strong
                                              >
                                            </td>
                                          </tr>
                                        </tbody>
                                      </table>
                                      <table
                                        style="
                                          width: 100%;
                                          border-spacing: 0;
                                          border-collapse: collapse;
                                          margin-top: 20px;
                                          border-top-width: 2px;
                                          border-top-color: #e5e5e5;
                                          border-top-style: solid;
                                        "
                                        class="row subtotal-table subtotal-table--total"
                                      >
                                        <tbody>
                                          <tr class="subtotal-line">
                                            <td
                                              style="
                                                font-family: -apple-system,
                                                  BlinkMacSystemFont, 'Segoe UI',
                                                  'Roboto', 'Oxygen', 'Ubuntu',
                                                  'Cantarell', 'Fira Sans',
                                                  'Droid Sans', 'Helvetica Neue',
                                                  sans-serif;
                                                padding: 20px 0 0;
                                              "
                                              class="subtotal-line__title"
                                            >
                                              <p
                                                style="
                                                  color: #777;
                                                  line-height: 1.2em;
                                                  font-size: 16px;
                                                  margin: 0;
                                                "
                                              >
                                                <span style="font-size: 16px"
                                                  >Total</span
                                                >
                                              </p>
                                            </td>
                                            <td
                                              align="right"
                                              style="
                                                font-family: -apple-system,
                                                  BlinkMacSystemFont, 'Segoe UI',
                                                  'Roboto', 'Oxygen', 'Ubuntu',
                                                  'Cantarell', 'Fira Sans',
                                                  'Droid Sans', 'Helvetica Neue',
                                                  sans-serif;
                                                padding: 20px 0 0;
                                              "
                                              class="subtotal-line__value"
                                            >
                                              <strong
                                                style="
                                                  font-size: 24px;
                                                  color: #555;
                                                "
                                                >{price} GBP</strong
                                              >
                                            </td>
                                          </tr>
                                        </tbody>
                                      </table>

                                      <p
                                        align="right"
                                        style="
                                          color: #777;
                                          line-height: 1.1;
                                          font-size: 16px;
                                          margin: 10px 0 0;
                                        "
                                        class="total-discount"
                                      >
                                        
                                        <span
                                          style="font-size: 16px; color: #555"
                                          class="total-discount--amount"
                                          ></span
                                        >
                                      </p>
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </center>
                  </td>
                </tr>
              </tbody>
            </table>

            <table
              style="width: 100%; border-spacing: 0; border-collapse: collapse"
              class="row section"
            >
              <tbody>
                <tr>
                  <td
                    style="
                      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI',
                        'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans',
                        'Droid Sans', 'Helvetica Neue', sans-serif;
                      padding: 40px 0;
                    "
                    class="section__cell"
                  >
                    <center>
                      <table
                        style="
                          width: 560px;
                          text-align: left;
                          border-spacing: 0;
                          border-collapse: collapse;
                          margin: 0 auto;
                        "
                        class="container"
                      >
                        <tbody>
                          <tr>
                            <td
                              style="
                                font-family: -apple-system, BlinkMacSystemFont,
                                  'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu',
                                  'Cantarell', 'Fira Sans', 'Droid Sans',
                                  'Helvetica Neue', sans-serif;
                              "
                            >
                              <h3
                                style="
                                  font-weight: normal;
                                  font-size: 20px;
                                  margin: 0 0 25px;
                                "
                              >
                                Customer information
                              </h3>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                      <table
                        style="
                          width: 560px;
                          text-align: left;
                          border-spacing: 0;
                          border-collapse: collapse;
                          margin: 0 auto;
                        "
                        class="container"
                      >
                        <tbody>
                          <tr>
                            <td
                              style="
                                font-family: -apple-system, BlinkMacSystemFont,
                                  'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu',
                                  'Cantarell', 'Fira Sans', 'Droid Sans',
                                  'Helvetica Neue', sans-serif;
                              "
                            >
                              <table
                                style="
                                  width: 100%;
                                  border-spacing: 0;
                                  border-collapse: collapse;
                                "
                                class="row"
                              >
                                <tbody>
                                  <tr>
                                    <td
                                      style="
                                        font-family: -apple-system,
                                          BlinkMacSystemFont, 'Segoe UI',
                                          'Roboto', 'Oxygen', 'Ubuntu',
                                          'Cantarell', 'Fira Sans', 'Droid Sans',
                                          'Helvetica Neue', sans-serif;
                                        padding-bottom: 40px;
                                        width: 50%;
                                      "
                                      class="customer-info__item"
                                    >
                                      <h4
                                        style="
                                          font-weight: 500;
                                          font-size: 16px;
                                          color: #555;
                                          margin: 0 0 5px;
                                        "
                                      >
                                        Contact information
                                      </h4>
                                      <p
                                        style="
                                          color: #777;
                                          line-height: 150%;
                                          font-size: 16px;
                                          margin: 0;
                                        "
                                      >
                                        {first_name} {last_name}<br />{email}<br />{phone}
                                      </p>
                                    </td>

                                    <td
                                      style="
                                        font-family: -apple-system,
                                          BlinkMacSystemFont, 'Segoe UI',
                                          'Roboto', 'Oxygen', 'Ubuntu',
                                          'Cantarell', 'Fira Sans', 'Droid Sans',
                                          'Helvetica Neue', sans-serif;
                                        padding-bottom: 40px;
                                        width: 50%;
                                      "
                                      class="customer-info__item"
                                    >
                                      <h4
                                        style="
                                          font-weight: 500;
                                          font-size: 16px;
                                          color: #555;
                                          margin: 0 0 5px;
                                        "
                                      >
                                        Billing address
                                      </h4>
                                      <p
                                        style="
                                          color: #777;
                                          line-height: 150%;
                                          font-size: 16px;
                                          margin: 0;
                                        "
                                      >
                                        {first_name} {last_name}<br />{house_num} {address}<br />{city}<br />{county}
                                        {postcode}<br />{residence}
                                      </p>
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                              <table
                                style="
                                  width: 100%;
                                  border-spacing: 0;
                                  border-collapse: collapse;
                                "
                                class="row"
                              >
                                <tbody>
                                  <tr>
                                    <td
                                      style="
                                        font-family: -apple-system,
                                          BlinkMacSystemFont, 'Segoe UI',
                                          'Roboto', 'Oxygen', 'Ubuntu',
                                          'Cantarell', 'Fira Sans', 'Droid Sans',
                                          'Helvetica Neue', sans-serif;
                                        padding-bottom: 40px;
                                        width: 50%;
                                      "
                                      class="customer-info__item"
                                    >
                                      <h4
                                        style="
                                          font-weight: 500;
                                          font-size: 16px;
                                          color: #555;
                                          margin: 0 0 5px;
                                        "
                                      >
                                        Shipping method
                                      </h4>
                                      <p
                                        style="
                                          color: #777;
                                          line-height: 150%;
                                          font-size: 16px;
                                          margin: 0;
                                        "
                                      >
                                        In-Hotel Pickup
                                      </p>
                                    </td>

                                    <td
                                      style="
                                        font-family: -apple-system,
                                          BlinkMacSystemFont, 'Segoe UI',
                                          'Roboto', 'Oxygen', 'Ubuntu',
                                          'Cantarell', 'Fira Sans', 'Droid Sans',
                                          'Helvetica Neue', sans-serif;
                                        padding-bottom: 40px;
                                        width: 50%;
                                      "
                                      class="customer-info__item"
                                    >
                                      <h4
                                        style="
                                          font-weight: 500;
                                          font-size: 16px;
                                          color: #555;
                                          margin: 0 0 5px;
                                        "
                                      >
                                        Payment method
                                      </h4>

                                      <p
                                        style="
                                          color: #777;
                                          line-height: 150%;
                                          font-size: 16px;
                                          margin: 0;
                                        "
                                        class="customer-info__item-content"
                                      >
                                        N/A
                                      </p>
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </center>
                  </td>
                </tr>
              </tbody>
            </table>

            <table
              style="
                width: 100%;
                border-spacing: 0;
                border-collapse: collapse;
                border-top-width: 1px;
                border-top-color: #e5e5e5;
                border-top-style: solid;
              "
              class="row footer"
            >
              <tbody>
                <tr>
                  <td
                    style="
                      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI',
                        'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans',
                        'Droid Sans', 'Helvetica Neue', sans-serif;
                      padding: 35px 0;
                    "
                    class="footer__cell"
                  >
                    <center>
                      <table
                        style="
                          width: 560px;
                          text-align: left;
                          border-spacing: 0;
                          border-collapse: collapse;
                          margin: 0 auto;
                        "
                        class="container"
                      >
                        <tbody>
                          <tr>
                            <td
                              style="
                                font-family: -apple-system, BlinkMacSystemFont,
                                  'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu',
                                  'Cantarell', 'Fira Sans', 'Droid Sans',
                                  'Helvetica Neue', sans-serif;
                              "
                            >
                              <p
                                style="
                                  color: #999;
                                  line-height: 150%;
                                  font-size: 14px;
                                  margin: 0;
                                "
                                class="disclaimer__subtext"
                              >
                                If you have any questions, contact us at
                                <a
                                  style="
                                    font-size: 14px;
                                    text-decoration: none;
                                    color: #000000;
                                  "
                                  href="mailto:nea@lukxee.com"
                                  >nea@lukxee.com</a
                                >
                              </p>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </center>
                  </td>
                </tr>
              </tbody>
            </table>
            <img
              style="min-width: 600px; height: 0"
              height="1"
              class="spacer"
              src="./spacer-1a26dfd5c56b21ac888f9f1610ef81191b571603cb207c6c0f564148473cab3c.png"
            />
          </td>
        </tr>
      </tbody>
    </table>
  </div>
  <div
    aria-hidden="true"
    id="cw-img-container-r1"
    style="overflow: hidden; height: 0px; width: 0px"
  >
  </div>
</body>
    '''
    rep = {"{order_num}": order_num, "{name}": name, "{root_url}": root_url, "{price}": price, "{first_name}": first_name, "{last_name}": last_name, "{email}": email, "{phone}": phone, "{house_num}": house_num, "{address}": address, "{city}": city, "{county}": county, "{postcode}": postcode, "{residence}": residence, "{type}": roomtype, "{checkin}": checkin, "{checkout}": checkout} # define desired replacements here
    # use these three lines to do the replacement
    rep = dict((re.escape(k), v) for k, v in rep.items()) 
    #Python 3 renamed dict.iteritems to dict.items so use rep.items() for latest versions
    pattern = re.compile("|".join(rep.keys()))
    html = pattern.sub(lambda m: rep[re.escape(m.group(0))], str)
    htmltext = MIMEText(html, 'html')
    msg.attach(htmltext)
    server.sendmail(sender, recipient, msg.as_string())
    server.quit()