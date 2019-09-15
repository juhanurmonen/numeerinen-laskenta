
# coding: utf-8

# # Numeerinen laskenta ja numpy-kirjasto

# ####### Kiinteä tietotyyppi, tehokas ja muistia säästävä; käyttää vierekkäisiä muistisoluja

# #### Perusasiat

# In[2]:


import numpy as np


# In[3]:


x = np.array([3,5,7])
print(x)


# In[4]:


x


# In[5]:


y=np.array([[13.0,7.5,10.7],[8.4,2.7,5.6]])
print(y)


# In[7]:


##### tämä pitää korjata
z=np.array([[[6,7,11],[3,28,0],[14,32,9],[21,8,2]],[[6,7,11],[41,30,15]],[[11,39],[0,4],[9,26],[2,15]])
print(z)


# In[8]:


##### dimensioiden lukumäärä
x.ndim


# In[9]:


y.ndim


# In[10]:


##### muoto
x.shape


# In[11]:


y.shape


# In[12]:


##### tietotyyppi
x.dtype


# In[13]:


y.dtype


# In[14]:


u=np.array([3,5,7])
u.dtype


# In[15]:


u=np.array([3,5,7], dtype='int16')
u.dtype


# In[16]:


##### koko
x.itemsize


# In[17]:


u.itemsize


# In[18]:


y.itemsize


# In[19]:


###### Koko yhteensä: numer of bytes = size * itemsize
x.size


# In[20]:


x.size*x.itemsize


# In[21]:


##### koko yhteensä
x.nbytes


# In[23]:


y.size


# In[24]:


y.size*y.itemsize


# #### Muutetaan solun arvoja, rivejä, sarakkeita

# In[25]:


#####
x = np.array([[11,12,13,14,15,16,17],[21,22,23,24,25,26,27]])
print(x)


# In[26]:


x.shape


# In[27]:


###### Haetaan tietyn solun arvo [rivi,sarake]
x[1,4]


# In[28]:


##### Sama solu laskien oikealta vasemmalle
x[1,-3]


# In[29]:


###### Haetaan tietty rivi
x[0,:]


# In[30]:


##### Haetaan tietty sarake
x[:,4]


# In[31]:


###### Haetaan [alkuindeksi:loppuindeksi:askelväli]
x[0,1:6:2]


# In[32]:


x[0,1:-1:2]


# In[33]:


###### Huomaa, että haku on poissulkeva
x[0,1:5:2]


# In[34]:


###### Sijoitetaan solun arvoksi haluttu
x[1,4]=77
print(x)


# In[35]:


##### Sijoitetaan rivin tai sarakkeen solujen arvoksi tietty arvo
x[:,3]=4
print(x)


# In[36]:


##### Sijoitetaan rivin tai sarakkeen solujen arvoiksi eri arvot
x[:,2]=[36,38]
print(x)


# In[38]:


##### Huomaa, että sijoittaessa ulottuvuuden on säilyttävä, muuten tulee virheilmoitus
x[:,-2]=[66,63,69]


# In[39]:


s=np.array([[[6,7,11],[3,28,0],[14,32,9],[21,8,2]],[[6,41],[7,30],[11,15]],[[2,9,0,11],[15,26,4,39]]])
print(s)


# In[40]:


s.ndim


# In[41]:


s.shape


# In[42]:


##### 3-D-esimerkki
v = np.array([[[11,12],[13,14]],[[15,16],[17,18]]])
print(v)


# In[43]:


##### Hae tietyn solun arvo
v[0,1,-1]


# In[44]:


##### Rivejä ja sarakkeita haetaan vastaavasti
v[:,1,:]


# In[45]:


v[:,1,0]


# In[46]:


##### Solujen arvon korvaaminen, säilytä ulottuvuudet
v[:,1,:]


# In[47]:


v[:,1,:] = [[3,4],[7,8]]
v


# In[48]:


##### Huom.
v[:,1,:] = [[3,4,8],[7,8,11]]


# In[49]:


##### Nollamatriiseja
np.zeros((4))


# In[50]:


np.zeros((4,3))


# In[51]:


np.zeros((4,3,2))


# In[52]:


np.zeros((4,3,2,3))


# In[53]:


np.zeros((3,2))


# In[54]:


##### Ykkösmatriiseja
np.ones((4,2,3))


# In[55]:


##### Muitakin argumentteja voi lisätä
np.ones((4,2,3), dtype='int32')


# In[56]:


##### Muut luvut
np.full((2,4), 47)


# In[57]:


np.full((2,4), 47, dtype='float32') 


# In[58]:


##### Olemassa olevan kaltainen
x.shape


# In[59]:


np.full(x.shape, 16)


# In[60]:


np.full_like(x, 16)


# In[61]:


##### Satunnaiset desimaaliluvut
np.random.rand(3,4)


# In[62]:


np.random.rand(4,2,3)


# In[63]:


np.random.random_sample(x.shape)


# In[64]:


##### Satunnaiset kokonaisluvut, 
np.random.randint(16)


# In[65]:


np.random.randint(16, size=(4,2))


# In[66]:


##### Huom. poissulkeva eli esim. seuraavassa arvot välillä 34-77 mahdollisia
np.random.randint(34, 78, size=(4,2))


# In[68]:


##### Toki negatiivisetkin luvut löytyvät
np.random.randint(-44, 78, size=(3,4))


# In[69]:


##### Identiteettimatriisi
np.identity(4)


# In[70]:


##### Toistoja
t1 = np.array([15,27,39])
r1 = np.repeat(t1,3)
print(r1)


# In[71]:


t2 = np.array([[15,27,39]])
r2 = np.repeat(t2,3, axis=0)
print(r2)


# In[74]:


r21 = np.repeat(t2,3, axis=1)
print(r21)


# In[78]:


##### Tehdään seuraava matriisi:
#####    1 1 1 1 1
#####    1 0 0 0 1
#####    1 0 6 0 1
#####    1 0 0 0 1
#####    1 1 1 1 1

matriisi = np.ones((5,5))
print(matriisi)
pieni = np.zeros((3,3))
print(pieni)


# In[81]:


##### Nyt meillä on iso matriisi ja pieni keskellä oleva.
##### Sijoitetaan pienemmän keskimäiseksi arvoksi kuusi ja
##### korvataan sitten isomman keskiosa pienemmällä matriisilla.

pieni[1,1]=6
matriisi[1:4,1:4]=pieni
print(matriisi)


# #### Numpy-taulukoiden (array) kopioinnissa huomioitavaa

# In[84]:


##### Katsotaanpas numpy-taulukkoa ja sen kopiota
taulu1 = np.array([6,16,26])
taulu2 = taulu1
taulu2[2] = -44
print(taulu1)


# In[85]:


##### Taulu2 siis osoittaa samaan paikkaan kuin taulu1 ja sijoitus muuttaa molempien taulujen solun arvon
##### taulun kopioiminen toiseksi tehdään .copy-toiminnolla

taulu3 = np.array([4,14,24])
taulu4 = taulu3.copy()
taulu4[2] = -66

print(taulu3)
print(taulu4)


# ### Aritmetiikkaa

# In[88]:


x = np.array([11,22,33,44,55])
print(x)


# In[90]:


x+10


# In[91]:


x-10


# In[92]:


x*10


# In[93]:


x/10


# In[98]:


# Voit toistaa operaatioita, kokeile toistuvasti esim.:

print(x)
x += 10
print(x)


# In[100]:


##### Yhteenlaskua ja muita perustoimintoja
s = np.array([10,20,30,40,50])
t = np.array([1,2,3,4,5])
s+t


# In[110]:


##### Tulo
s*t


# In[101]:


##### Toinen potenssi
s**2


# In[107]:


##### Kosini ja muita trigonometrisiö operaatioita
np.cos(s)


# In[108]:


np.sin(s)


# In[104]:


np.tan(t)


# ##### Ja tietenkin paljon muuta, ks.
# https://docs.scipy.org/doc/numpy/reference/routines.math.html

# ### Lineaarialgebra

# In[112]:


m = np.ones([3,4])
print(m)


# In[113]:


n = np.full([4,3],4)
print(n)


# In[114]:


#### Tulo ei nyt onnistu, koska ovat eri tyyppiä, esim.
m*n


# In[116]:


##### Otetaan siis matriisien tulo kuten lineaarialgebrassa
##### Huomaa, että tuloksena on 3x3-matriisi, johtuen m:stä ja n:stä
np.matmul(m,n)


# In[117]:


##### Determinantin etsiminen
i = np.identity(4)
np.linalg.det(i)


# ##### Ja paljon lisää, ks.
# https://docs.scipy.org/doc/numpy/reference/routines.linalg.html

# ### Tilastomatematiikkaa
