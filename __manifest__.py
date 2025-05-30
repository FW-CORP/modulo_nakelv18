{
    "name": "Etiquetas de Stock (ES-AR) – vistas",
    "version": "18.0.2.0.2",
    "summary": "Reemplaza visualmente 'On Hand/A la mano' → 'Stock' y 'Forecasted/Pronosticado' → 'Ingreso' (solo español)",
    "author": "Intaky Dev",
    "license": "AGPL-3",
    "category": "Localization",
    "depends": [
	"stock", 
	"product",
	"account",
	"l10n_ar"
     ],
    "data": [
        "views/stock_views.xml",
	"data/taxes.xml",
	"data/tax_groups.xml",
    ],
    "installable": True,
}
