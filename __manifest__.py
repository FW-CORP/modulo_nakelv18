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
        "point_of_sale",
        "l10n_ar_pos",
    ],
    "data": [
        "views/stock_views.xml",
        "views/modify_pos.xml"
    ],
    "installable": True,
}