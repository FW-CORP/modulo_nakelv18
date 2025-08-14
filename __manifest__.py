{
    "name": "Etiquetas POS y Stock ES",
    "version": "18.0.1.0.0",
    "author": "Intaky Dev",
    "license": "AGPL-3",
    "category": "Localization",
    "depends": [
        "stock",
        "product",
        "point_of_sale",
        "l10n_ar_pos"
    ],
    "data": [
        "views/stock_views.xml",
        "views/pos_templates.xml"
    ],
    "assets": {
        "point_of_sale_assets": [
            "modulo_nakelv18/static/src/js/pos_custom.js",
        ]
    },
    "installable": True
}