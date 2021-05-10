class Hora: 
     __seg=0
     __minut=0
     __hora=0

     def __init__(self, hora=0,minut=0,seg=0):
        if self.validarHora(hora,minut,seg):
            self.__hora = hora
            self.__minut = minut
            self.__seg = seg
        else: 
         print("Los datos han sido ingresado de forma incorrecta reinicie el programa y coloquelos de forma correcta")   
         sys.exit()

     def validarHora(self,hora,minut,seg):
        band=False 
        if (hora<24 and minut<60 and seg<60): 
           band= True 
        return band


     def Mostrar (self):
       print (f'{self.__hora}:{self.__minut}:{self.__seg}')
     def getHora(self):
        return self.__hora

     def getMinutos(self):
        return self.__minut

     def getSegundos(self):
        return self.__seg
     def validarHora(self,hora,minut,seg):
      band=False 
      if (hora<24 and minut<60 and seg<60): 
        band= True 
      return band