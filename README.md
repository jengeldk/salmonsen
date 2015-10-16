# Salmonsen
Her er alle tekstfilerne fra [Salmonsens Leksikon, anden Udgave](http://runeberg.org/salmonsen/2/),
de er hentet fra http://runeberg.org den 14/9 2015.

Intentionen er at finde fejl i opmærkningen og evt. fejl i digitaliseringen. Der skal laves lister over
forfattere med links til deres artikler. Der er også lavet lister over stavefejl mm. i leksikonnet.

Rettelserne vil løbende blive indført på github - og om muligt tilbageført til http://runeberg.org

Der er to branches: `master` som er der hvor rettelserne bliver indført og `runeberg` som indeholder
teksten fra http://runeberg.org. `runeberg` er opdateret fra http://runeberg.org 14/10 2015. Rettelser fra
`runeberg` er merged ind i `master`. Status for antal rettelser er:

    git diff --shortstat  runeberg master -- '*/[0-1]*.txt'
    2568 files changed, 35711 insertions(+), 25349 deletions(-)

Det betyder at 25349 linier er ændret på 2568 sider.
