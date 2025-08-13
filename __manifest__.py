{
    "name": "Etiquetas de Stock (ES-AR) – vistas",
    "version": "18.0.2.0.2",
    "summary": "Reemplaza visualmente 'On Hand/A la mano' → 'Stock' y 'Forecasted/Pronosticado' → 'Ingreso' en las vistas de inventario.",
    "author": "Intaky Dev",
    "license": "AGPL-3",
    "category": "Localization",
    "depends": [
	"stock", 
	"product",
	"account",
    "web",
     ],
    "data": [
        "views/stock_views.xml"
        "views/user_menu_views.xml",
    ],
    "installable": True,
}
