
# coding: utf-8

# # Numeerinen laskenta ja numpy-kirjasto

# ####### Kiinteä tietotyyppi, tehokas ja muistia säästävä; käyttää vierekkäisiä muistisoluja

# #### Perusasiat

# In[1]:


import numpy as np


# In[2]:


x = np.array([3,5,7])
print(x)


# In[3]:


x


# In[4]:


y=np.array([[13.0,7.5,10.7],[8.4,2.7,5.6]])
print(y)


# In[5]:


##### dimensioiden lukumäärä
x.ndim


# In[6]:


y.ndim


# In[7]:


##### muoto
x.shape


# In[8]:


y.shape


# In[9]:


##### tietotyyppi
x.dtype


# In[10]:


y.dtype


# In[11]:


u=np.array([3,5,7])
u.dtype


# In[12]:


u=np.array([3,5,7], dtype='int16')
u.dtype


# In[13]:


##### koko
x.itemsize


# In[14]:


u.itemsize


# In[15]:


y.itemsize


# In[16]:


###### Koko yhteensä: numer of bytes = size * itemsize
x.size


# In[17]:


x.size*x.itemsize


# In[18]:


##### koko yhteensä
x.nbytes


# In[19]:


y.size


# In[20]:


y.size*y.itemsize


# #### Muutetaan solun arvoja, rivejä, sarakkeita

# In[21]:


#####
x = np.array([[11,12,13,14,15,16,17],[21,22,23,24,25,26,27]])
print(x)


# In[22]:


x.shape


# In[23]:


###### Haetaan tietyn solun arvo [rivi,sarake]
x[1,4]


# In[24]:


##### Sama solu laskien oikealta vasemmalle
x[1,-3]


# In[25]:


###### Haetaan tietty rivi
x[0,:]


# In[26]:


##### Haetaan tietty sarake
x[:,4]


# In[27]:


###### Haetaan [alkuindeksi:loppuindeksi:askelväli]
x[0,1:6:2]


# In[28]:


x[0,1:-1:2]


# In[29]:


###### Huomaa, että haku on poissulkeva
x[0,1:5:2]


# In[30]:


###### Sijoitetaan solun arvoksi haluttu
x[1,4]=77
print(x)


# In[31]:


##### Sijoitetaan rivin tai sarakkeen solujen arvoksi tietty arvo
x[:,3]=4
print(x)


# In[32]:


##### Sijoitetaan rivin tai sarakkeen solujen arvoiksi eri arvot
x[:,2]=[36,38]
print(x)


# In[33]:


##### Huomaa, että sijoittaessa ulottuvuuden on säilyttävä, muuten tulee virheilmoitus
x[:,-2]=[66,63,69]


# In[34]:


##### 3-D-esimerkki
v = np.array([[[11,12],[13,14]],[[15,16],[17,18]]])
print(v)


# In[35]:


##### Hae tietyn solun arvo
v[0,1,-1]


# In[36]:


##### Rivejä ja sarakkeita haetaan vastaavasti
v[:,1,:]


# In[37]:


v[:,1,0]


# In[38]:


##### Solujen arvon korvaaminen, säilytä ulottuvuudet
v[:,1,:]


# In[39]:


v[:,1,:] = [[3,4],[7,8]]
v


# In[40]:


##### Huom.
v[:,1,:] = [[3,4,8],[7,8,11]]


# In[41]:


##### Nollamatriiseja
np.zeros((4))


# In[42]:


np.zeros((4,3))


# In[43]:


np.zeros((4,3,2))


# In[44]:


np.zeros((4,3,2,3))


# In[45]:


np.zeros((3,2))


# In[46]:


##### Ykkösmatriiseja
np.ones((4,2,3))


# In[47]:


##### Muitakin argumentteja voi lisätä
np.ones((4,2,3), dtype='int32')


# In[48]:


##### Muut luvut
np.full((2,4), 47)


# In[49]:


np.full((2,4), 47, dtype='float32') 


# In[50]:


##### Olemassa olevan kaltainen
x.shape


# In[51]:


np.full(x.shape, 16)


# In[52]:


np.full_like(x, 16)


# In[53]:


##### Satunnaiset desimaaliluvut
np.random.rand(3,4)


# In[54]:


np.random.rand(4,2,3)


# In[55]:


np.random.random_sample(x.shape)


# In[56]:


##### Satunnaiset kokonaisluvut, 
np.random.randint(16)


# In[57]:


np.random.randint(16, size=(4,2))


# In[58]:


##### Huom. poissulkeva eli esim. seuraavassa arvot välillä 34-77 mahdollisia
np.random.randint(34, 78, size=(4,2))


# In[59]:


##### Toki negatiivisetkin luvut löytyvät
np.random.randint(-44, 78, size=(3,4))


# In[60]:


##### Identiteettimatriisi
np.identity(4)


# In[61]:


##### Toistoja
t1 = np.array([15,27,39])
r1 = np.repeat(t1,3)
print(r1)


# In[62]:


t2 = np.array([[15,27,39]])
r2 = np.repeat(t2,3, axis=0)
print(r2)


# In[63]:


r21 = np.repeat(t2,3, axis=1)
print(r21)


# ##### Tehdään seuraava matriisi
# 
# <table>
#     <tr><td>8</td><td>8</td><td>8</td><td>8</td><td>8</td></tr>
#     <tr><td>8</td><td>0</td><td>0</td><td>0</td><td>8</td></tr>
#     <tr><td>8</td><td>0</td><td>6</td><td>0</td><td>8</td></tr>
#     <tr><td>8</td><td>0</td><td>0</td><td>0</td><td>8</td></tr>
#     <tr><td>8</td><td>8</td><td>8</td><td>8</td><td>8</td></tr>
# </table>

# In[64]:


matriisi = np.full((5,5),8)
print(matriisi)
pieni = np.zeros((3,3))
print(pieni)


# In[65]:


##### Nyt meillä on iso matriisi ja pieni keskellä oleva.
##### Sijoitetaan pienemmän keskimäiseksi arvoksi kuusi ja
##### korvataan sitten isomman keskiosa pienemmällä matriisilla.

pieni[1,1]=6
matriisi[1:4,1:4]=pieni
print(matriisi)


# #### Numpy-taulukoiden (array) kopioinnissa huomioitavaa

# In[66]:


##### Katsotaanpas numpy-taulukkoa ja sen kopiota
taulu1 = np.array([6,16,26])
taulu2 = taulu1
taulu2[2] = -44
print(taulu1)


# In[67]:


##### Taulu2 siis osoittaa samaan paikkaan kuin taulu1 ja sijoitus muuttaa molempien taulujen solun arvon
##### taulun kopioiminen toiseksi tehdään .copy-toiminnolla

taulu3 = np.array([4,14,24])
taulu4 = taulu3.copy()
taulu4[2] = -66

print(taulu3)
print(taulu4)


# ### Aritmetiikkaa

# In[68]:


x = np.array([11,22,33,44,55])
print(x)


# In[69]:


x+10


# In[70]:


x-10


# In[71]:


x*10


# In[72]:


x/10


# In[73]:


# Voit toistaa operaatioita, kokeile toistuvasti esim.:

print(x)
x += 10
print(x)


# In[74]:


##### Yhteenlaskua ja muita perustoimintoja
s = np.array([10,20,30,40,50])
t = np.array([1,2,3,4,5])
s+t


# In[75]:


##### Tulo
s*t


# In[76]:


##### Toinen potenssi
s**2


# In[77]:


##### Kosini ja muita trigonometrisiö operaatioita
np.cos(s)


# In[78]:


np.sin(s)


# In[79]:


np.tan(t)


# ##### Ja tietenkin paljon muuta, ks.
# https://docs.scipy.org/doc/numpy/reference/routines.math.html

# ### Lineaarialgebraa

# In[80]:


m = np.ones([3,4])
print(m)


# In[81]:


n = np.full([4,3],4)
print(n)


# In[82]:


#### Tulo ei nyt onnistu, koska ovat eri tyyppiä, esim.
m*n


# In[83]:


##### Otetaan siis matriisien tulo kuten lineaarialgebrassa
##### Huomaa, että tuloksena on 3x3-matriisi, johtuen m:stä ja n:stä
np.matmul(m,n)


# In[84]:


##### Determinantin etsiminen
i = np.identity(4)
np.linalg.det(i)


# ##### Ja paljon lisää, ks.
# https://docs.scipy.org/doc/numpy/reference/routines.linalg.html

# ### Tilastomatematiikkaa

# In[85]:


tilasto = np.array([[11,24,37],[22,25,28]])
tilasto


# In[86]:


##### Minimiarvo
np.min(tilasto)


# In[87]:


##### Maksimiarvo
np.max(tilasto)


# In[88]:


##### Riveittäin
np.min(tilasto, axis=1)


# In[89]:


##### Sarakkeittain
np.min(tilasto, axis=0)


# In[90]:


np.max(tilasto, axis=0)


# In[91]:


##### Muita operaatioita
np.sum(tilasto)


# In[92]:


np.sum(tilasto,axis=0)


# In[93]:


np.sum(tilasto,axis=1)


# In[94]:


np.percentile(tilasto,0.4,axis=0)


# In[95]:


np.percentile(tilasto,0.4,axis=1)


# ##### Ja paljon lisää,ks.
# https://docs.scipy.org/doc/numpy/reference/routines.statistics.html

# ##### Numpy-taulukon uudelleenmuotoiluja

# In[96]:


taulu20 = np.array([[20,30,40,50],[60,70,80,90]])
print(taulu20)


# In[97]:


taulu81 = taulu20.reshape([8,1])
print(taulu81)


# In[98]:


taulu18 = taulu20.reshape([1,8])
print(taulu18)


# In[99]:


taulu42 = taulu20.reshape([4,2])
print(taulu42)


# In[100]:


taulu222 = taulu20.reshape([2,2,2])
print(taulu222)


# In[101]:


##### Arvojen lukumäärän tulee säilyä, muuten tulee virheilmoitus
taulu23 = taulu20.reshape([2,3])
print(taulu23)


# In[102]:


##### Pystysuuntaiset pinovektorit vstack
vec1 = np.array([11,21,31])
vec2 = np.array([12,22,32])

print(vec1)
print(vec2)


# In[103]:


np.vstack([vec1,vec2])


# In[104]:


np.vstack([vec1,vec1,vec2,vec2])


# In[105]:


##### Huom. Vektoreiden kokojen tulee olla samanlaiset:

vec3 = np. array([33,43,53,63,73])

np.vstack([vec2,vec3])


# In[106]:


###### Vaakasuuntaiset pinovektorit hstack

np.hstack([vec1,vec3])


# In[107]:


hor1 = np.ones((2,4))
print(hor1)


# In[108]:


hor2 = np.zeros((2,2))
print(hor2)


# In[109]:


np.hstack((hor1,hor2))


# In[110]:


np.hstack([hor1,hor2])


# ### Muuta huomattavaa

# #### Data tiedostosta

# In[111]:


##### Seuraava yksinkertainen data on txt-tiedostossa osoitteessa
##### http://myy.haaga-helia.fi/~digiosaaja/digipiiri/data/numpy-data-tekstitiedostosta.txt

##### Tässä data on samassa muodossa kuin tiedostossa, genfromtxt huolehtii rivinvaihdosta

tdstodata = np.genfromtxt('http://myy.haaga-helia.fi/~digiosaaja/digipiiri/data/numpy-data-tekstitiedostosta.txt', delimiter=',')
print(tdstodata)


# In[112]:


##### Datatyyppi on automaattisesti float.
##### Datatyypin voi muuttaa astype-komennolla

tdstodata.astype('int32')


# In[113]:


##### Huom. astype tekee kopion alkuperäisesti, eri tietotyypit kun vievät eri määrän tilaa:
##### Alkuperäinen on siis vieläkin tyyppiä float:

tdstodata


# In[114]:


##### Alkuperäinen muuttuu vasa sijoittamalla

tdstodata = tdstodata.astype('int32')
tdstodata


# #### Boolean-arvot ja edistyneempää indeksöintiä

# In[115]:


print(tdstodata)


# In[116]:


##### Testataan totuusarvoja

tdstodata > 80


# In[117]:


tdstodata <= 92


# In[118]:


##### Etsitään ehdot toteuttavat arvot
##### Tässä siis indeksöidään ehdon mukaisesti

tdstodata[tdstodata > 70]


# In[119]:


##### NumPy:ssä voi nimittäin indeksöidä listalla:

k = np.array([11,22,33,44,55,66,77,88,99])

##### Valitaan tästä 44, 55 ja 88:

k[[3,4,7]]


# In[120]:


k[[3,4,-2]]


# In[121]:


##### Indeksöinnin sovelluksia, any

np.any(tdstodata > 70, axis=0)


# In[122]:


np.any(tdstodata > 70, axis=1)


# In[123]:


##### Indeksöinnin sovelluksia, all

np.all(tdstodata < 70, axis=0)


# In[124]:


np.all(tdstodata < 150, axis=1)


# In[125]:


##### Lisää totuusarvojen testamista

((tdstodata > 40) & (tdstodata < 100))


# In[126]:


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

# In[127]:


h = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]])
print(h)


# In[128]:


h[2:4,0:2]


# In[129]:


h[[0,1,2,3],[1,2,3,4]]


# In[130]:


h[[0,4,5],3:]


# In[131]:


##### Lopuksi vielä tiedostonkäsittelyä: tallennus
##### Tiedosto tallentuu samaan hakemistoon, mihin Python on asennettu

np.save('harjoitus',h)


# In[132]:


##### Tiedoston lataaminen:

np.load('harjoitus.npy')


# Lähteinä käytetty: <br> <a href="https://youtu.be/QUT1VHiLmmI">Keith Galli: Python NumPy Tutorial for Beginners</a> (YouTube) <br>
# <a href="https://youtu.be/uQsLXB1Pmqk">The Top 5 Machine Learning Libraries in Python</a> (YouTube)
