import network


class RedeW:

    def __init__(self):
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        
    def connect_wifi(self, ssid, password):
        """
        Conecta-se a rede wifi

        Parametros:
            ssid: nome da rede wifi
            password: senha da rede wifi
        """
        if True:  
            print('Connecting to network...')
            self.wlan.connect(ssid, password)  
            
            while not self.wlan.isconnected():  
                pass
            
            print('Network config:', self.wlan.ifconfig())
        #else:
            #print('Already connected.')
            
    def disconnect_wifi(self):
        """
        Desconecta da rede wifi atual.
        """
        if self.wlan.isconnected():
            self.wlan.disconnect()
            print('Disconnected from network.')
        else:
            print('No network to disconnect from.')
            
    def check_connection(self):
        """
        Verifica se o dispositivo está conectado a uma rede wifi.
        """
        if self.wlan.isconnected():
            print('Connected to network.')
            return True
        else:
            print('Not connected to any network.')
            return False

    def connect_using_credentials(self):
        """
        Conecta-se a rede wifi utilizando as credenciais informadas pelo usuário.
        """
        ssid = input('Enter the SSID of your network: ')
        password = input('Enter the password of your network: ')
        self.connect_wifi(ssid, password)
        
    def show_connection_info(self):
        """
        Exibe informações sobre a conexão Wi-Fi atual.
        """
        if self.check_connection():
            print("\n========== Wi-Fi Connection Info ==========")
            print(f"SSID: {self.wlan.config('essid')}")
            ip, netmask, gateway, dns = self.wlan.ifconfig()
            print(f"IP Address: {ip}")
            print(f"Netmask: {netmask}")
            print(f"Gateway: {gateway}")
            print(f"DNS: {dns}")
            print("===========================================\n")
        else:
            print("Not connected to any network.")

