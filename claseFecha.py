import sys 
from claseHora import Hora
class FechaHora:
    __dia=0
    __mes=0
    __año=0
    __seg=0
    __minut=0
    __hora=0
    def __init__(self,dia=1,mes=1,año=2020,hora=0,minut=0,seg=0):
       if  self.validarFecha(dia,mes,año) and self.validarHora(hora,minut,seg):
        self.__dia=dia
        self.__mes=mes
        self.__año=año
        self.__hora=hora
        self.__minut=minut
        self.__seg=seg
       else: 
         print("Los datos han sido ingresado de forma incorrecta reinicie el programa y coloquelos de forma correcta")   
         sys.exit()

    def cambiarFecha(self):
       if self.__seg>60:
        self.__minut+=self.__seg//60
        self.__seg=self.__seg%60
       if self.__minut>=60:
        self.__hora+=self.__minut//60
        self.__minut=self.__minut%60
       if self.__hora>=24:
         self.__dia+=self.__hora//24
         self.__hora=self.__hora%24
       if self.__mes in [1,3,5,8,10,12]:
         if self.__dia>31:
            self.__mes+=self.__dia//31
            self.__dia=self.__dia%31
       elif self.__mes in [4,6,7,9,11]:
         if self.__dia>30:
            self.__mes+=self.__dia//30
            self.__dia=self.__dia%30

       else: 
           bisiesto=False
           if self.__año%4==0:
               if self.__año%100==0:
                   if self.__año%400==0: 
                     bisiesto=True

           if bisiesto==True:
             if self.__dia>=29:
              self.__mes+=self.__dia//29
              self.__dia=self.__dia%29
           else:
             if self.__dia>=28:
              self.__mes+=self.__dia//28
              self.__dia=self.__dia%28
       if  self.__mes>=12:
           self.__año+=self.__mes//24
           self.__mes-self.__mes%24
         
       if self.__mes==13:
              self.__mes=1
              self.__año=self.__año+1
    def PonerEnHora(self,hora=0,minut=0,seg=0): 
         self.__hora=hora
         self.__minut=minut
         self.__seg=seg
    def AdelantarHora(self,hora=0,minut=0,seg=0):
        self.__hora+=hora
        self.__minut+= minut
        self.__seg+=seg
        self.cambiarFecha()   
    def Mostrar (self):
     print ( "    H:M:S-------D/M/A")
     print (f"  {self.__hora}:{self.__minut}:{self.__seg}-------{self.__dia}/{self.__mes}/{self.__año}") 
     
    def validarHora(self,hora,minut,seg):
      band=False 
      if (hora<24 and minut<60 and seg<60): 
        band= True 
      return band
    def validarFecha(self,dia,mes,año):
       band=False 
       if (dia <= 31 and dia>=1 and (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12)) or (self.__dia <= 30 and (mes==4 or mes==6 or mes==9 or mes==11)) or (dia<=28 and mes==2) or (mes==2 and dia<=29 and (((año%4) == 0) or (((año%100) == 0) and (año%400) == 0))):   
          band= True 
       return band 
    def getDia (self):
        return self.__dia
    
    def getMes (self):
        return self.__mes

    def getAño (self):
        return self.__año

    def getHora(self):
        return self.__hora

    def getMinutos(self):
        return self.__minut

    def getSegundos(self):
        return self.__seg
    def __add__(self, unaHora):
        aux=Hora()
        if type (aux) == type(unaHora):
            FechaRes = FechaHora(self.getDia(), self.getMes(), self.getAño(),self.getHora()+unaHora.getHora(),self.getMinutos()+unaHora.getMinutos(),self.getSegundos()+unaHora.getSegundos())
            return FechaRes

    def __radd__(self, dato):
        aux=Hora()
        if type (aux) == type(dato):
            FechaRes = FechaHora(self.getDia(), self.getMes(), self.getAño(),self.getHora()+dato.getHora(),self.getMinutos()+dato.getMinutos(),self.getSegundos()+dato.getSegundos())
            return FechaRes
        elif type (dato) == int:
            FechaRes = FechaHora(self.getDia()+dato, self.getMes(), self.getAño(),self.getHora(),self.getMinutos(),self.getSegundos())
            return FechaRes
    
    def __sub__(self, dias):
        if type(dias) == int:
            FechaRes = FechaHora(self.getDia()-dias, self.getMes(), self.getAño(),self.getHora(),self.getMinutos(),self.getSegundos())
            return FechaRes

  

        