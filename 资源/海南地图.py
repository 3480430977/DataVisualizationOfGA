import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
# 东经108°37′—111°03′，北纬18°10′—20°10′
# figsize=((111+3/60-108+37/60), (20+10/60-18+10/60))
plt.figure(figsize=((111+3/60-108+37/60), (20+10/60-18+10/60)), dpi=320)
m = Basemap(llcrnrlon=108+37/60, llcrnrlat=18+10/60, urcrnrlon=111+3/60, urcrnrlat=20+10/60)
m.readshapefile('map/gadm36_CHN_3', 'states', drawbounds=True)
plt.show()
