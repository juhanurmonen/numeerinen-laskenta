
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


# In[240]:


z=np.array[[[6,41],[7,30],[11,15]],
             [[3,15],[28,7],[0,4]],
            [[14,9],[32,3],[9,26]],
            [[21,13],[8,11],[2,15]]]


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

# ### Lineaarialgebraa

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

# In[134]:


tilasto = np.array([[11,24,37],[22,25,28]])
tilasto


# In[135]:


##### Minimiarvo
np.min(tilasto)


# In[136]:


##### Maksimiarvo
np.max(tilasto)


# In[137]:


##### Riveittäin
np.min(tilasto, axis=1)


# In[139]:


##### Sarakkeittain
np.min(tilasto, axis=0)


# In[140]:


np.max(tilasto, axis=0)


# In[141]:


##### Muita operaatioita
np.sum(tilasto)


# In[142]:


np.sum(tilasto,axis=0)


# In[143]:


np.sum(tilasto,axis=1)


# ##### Numpy-taulukon uudelleenmuotoiluja

# In[148]:


taulu20 = np.array([[20,30,40,50],[60,70,80,90]])
print(taulu20)


# In[149]:


taulu81 = taulu20.reshape([8,1])
print(taulu81)


# In[150]:


taulu18 = taulu20.reshape([1,8])
print(taulu18)


# In[151]:


taulu42 = taulu20.reshape([4,2])
print(taulu42)


# In[152]:


taulu222 = taulu20.reshape([2,2,2])
print(taulu222)


# In[153]:


##### Arvojen lukumäärän tulee säilyä, muuten tulee virheilmoitus
taulu23 = taulu20.reshape([2,3])
print(taulu23)


# In[157]:


##### Pystysuuntaiset pinovektorit vstack
vec1 = np.array([11,21,31])
vec2 = np.array([12,22,32])

print(vec1)
print(vec2)


# In[158]:


np.vstack([vec1,vec2])


# In[160]:


np.vstack([vec1,vec1,vec2,vec2])


# In[161]:


##### Huom. Vektoreiden kokojen tulee olla samanlaiset:

vec3 = np. array([33,43,53,63,73])

np.vstack([vec2,vec3])


# In[163]:


###### Vaakasuuntaiset pinovektorit hstack

np.hstack([vec1,vec3])


# In[167]:


hor1 = np.ones((2,4))
print(hor1)


# In[169]:


hor2 = np.zeros((2,2))
print(hor2)


# In[171]:


np.hstack((hor1,hor2))


# In[172]:


np.hstack([hor1,hor2])


# ### Muuta huomattavaa

# #### Data tiedostosta

# In[179]:


##### Seuraava yksinkertainen data on txt-tiedostossa osoitteessa
##### http://myy.haaga-helia.fi/~digiosaaja/digipiiri/data/numpy-data-tekstitiedostosta.txt

##### Tässä data on samassa muodossa kuin tiedostossa, genfromtxt huolehtii rivinvaihdosta

tdstodata = np.genfromtxt('http://myy.haaga-helia.fi/~digiosaaja/digipiiri/data/numpy-data-tekstitiedostosta.txt', delimiter=',')
print(tdstodata)


# In[180]:


##### Datatyyppi on automaattisesti float.
##### Datatyypin voi muuttaa astype-komennolla

tdstodata.astype('int32')


# In[181]:


##### Huom. astype tekee kopion alkuperäisesti, eri tietotyypit kun vievät eri määrän tilaa:
##### Alkuperäinen on siis vieläkin tyyppiä float:

tdstodata


# In[182]:


##### Alkuperäinen muuttuu vasa sijoittamalla

tdstodata = tdstodata.astype('int32')
tdstodata


# #### Boolean-arvot ja edistyneempää indeksöintiä

# In[183]:


print(tdstodata)


# In[185]:


##### Testataan totuusarvoja

tdstodata > 80


# In[189]:


tdstodata <= 92


# In[191]:


##### Etsitään ehdot toteuttavat arvot
##### Tässä siis indeksöidään ehdon mukaisesti

tdstodata[tdstodata > 70]


# In[193]:


##### NumPy:ssä voi nimittäin indeksöidä listalla:

k = np.array([11,22,33,44,55,66,77,88,99])

##### Valitaan tästä 44, 55 ja 88:

k[[3,4,7]]


# In[194]:


k[[3,4,-2]]


# In[195]:


##### Indeksöinnin sovelluksia, any

np.any(tdstodata > 70, axis=0)


# In[196]:


np.any(tdstodata > 70, axis=1)


# In[197]:


##### Indeksöinnin sovelluksia, all

np.all(tdstodata < 70, axis=0)


# In[201]:


np.all(tdstodata < 150, axis=1)


# In[203]:


##### Lisää totuusarvojen testamista

((tdstodata > 40) & (tdstodata < 100))


# In[205]:


##### Negaatio on ~; äskeinen toisin päin:

~((tdstodata > 40) & (tdstodata < 100))


# ##### Harjoitellaan indeksejä
# 
# Otetaan käsittelyyn seuraava taulu:
#   

# <table>
# 
# <tr align="center"><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr>
# 
# <tr align="center"><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr>
# 
# <tr align="center"><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td></tr>
# 
# <tr align="center"><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td></tr>
# 
# <tr align="center"><td>21</td><td>22</td><td>23</td><td>24</td><td>25</td></tr>
# 
# <tr align="center"><td>26</td><td>27</td><td>28</td><td>29</td><td>30</td></tr>
# 
# </table>

# Millä koodilla tästä saa ulos matriisin:
# 
# <table>
# <tr align="center"><td>11</td><td>12</td></tr>
# <tr align="center"><td>16</td><td>17</td></tr>
# </table>

# Entä solut, jotka tässä sisältävät luvut 2, 8, 14, 20?

# Entä solut, jotka sisältävät luvut 4, 5, 24, 25, 29 ja 30?

# In[216]:


h = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]])
print(h)


# In[218]:


h[2:4,0:2]


# In[223]:


h[[0,1,2,3],[1,2,3,4]]


# In[228]:


h[[0,4,5],3:]


# In[230]:


##### Lopuksi vielä tiedostonkäsittelyä: tallennus
##### Tiedosto tallentuu samaan hakemistoon, mihin Python on asennettu

np.save('h',h)


# In[232]:


##### Tiedoston lataaminen:

np.load('h.npy')


# Lähteinä käytetty: <br> <a href="https://youtu.be/QUT1VHiLmmI">Keith Galli: Python NumPy Tutorial for Beginners</a> (YouTube) <br>
# <a href="https://youtu.be/uQsLXB1Pmqk">The Top 5 Machine Learning Libraries in Python</a> (YouTube)
