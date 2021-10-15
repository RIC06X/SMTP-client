from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    # Fill in start
    # Fill in end
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    recv = clientSocket.recv(1024).decode()
    # print(recv)
    # if recv[:3] != '220':
    #     print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)
    # if recv1[:3] != '250':
    #     print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    # Fill in end
    From = "MAIL FROM: <alice@crepes.fr>\r\n"
    clientSocket.send(From.encode())
    recv2 = clientSocket.recv(1024).decode()
    # print(recv2)
    # if recv2[:3] != '250':
    #     print('250 reply not received from server.')

    # Send RCPT TO command and print server response.
    # Fill in start
    # Fill in end
    To = "RCPT TO: <bob@hamburger.edu>\r\n"
    clientSocket.send(To.encode())
    recv3 = clientSocket.recv(1024).decode()
    # print(recv3)
    # if recv3[:3] != '250':
    #     print('250 reply not received from server.')

    # Send DATA command and print server response.
    # Fill in start
    # Fill in end
    Data = "DATA\r\n"
    clientSocket.send(Data.encode())
    recv4 = clientSocket.recv(1024).decode()
    # print(recv4)
    # if recv4[:3] != '354':
    #     print('354 error')

    # Send message data.
    # Fill in start
    # Fill in end
    clientSocket.send(msg.encode())


    # Message ends with a single period.
    # Fill in start
    # Fill in end
    clientSocket.send(endmsg.encode())
    # recv5 = clientSocket.recv(1024).decode()
    # print(recv5)


    # Send QUIT command and get server response.
    # Fill in start
    # Fill in end
    clientSocket.send("QUIT\r\n".encode())
    recv6 = clientSocket.recv(1024).decode()

    clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
