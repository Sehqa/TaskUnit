class ListMet(object):


    #Метод для сравнения списков
    def _compars_mass(a,b):
        for i in range(0, len(a)):
            if (a[i]!=b[i]):
                 return(a[i],b[i])


