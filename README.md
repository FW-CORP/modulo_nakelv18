Impuestos Internos (AR)
======================

Este módulo crea automáticamente el grupo y las alícuotas de Impuestos Internos,
las declara con el código AFIP 04 y las hace parte de la base del IVA.
Además, permite asignar una alícuota por categoría de producto para que los
productos hereden el impuesto sin intervención manual.

Instalación
-----------
1. Copiá la carpeta ``impuestos_internos`` en tu ruta de addons.
2. En **Aplicaciones**, actualizá la lista y buscá "Impuestos Internos (AR)".
3. Instalá el módulo.

Uso rápido
----------
* Editá tus **categorías de producto** y seleccioná la alícuota interna.
* Al crear un producto nuevo (o cambiar su categoría) se asignará el impuesto.
* Emití una factura de prueba y verificá que:
  - Aparezca la línea de II y luego el IVA calculado sobre subtotal + II.
  - El XML de AFIP incluya `<IdTributo>04</IdTributo>`.

Actualización de alícuotas
-------------------------
Para añadir o modificar tasas:
1. Duplica uno de los bloques `<record>` en ``data/impuestos_internos.xml``.
2. Cambiá el valor `<field name="amount">` y el `id` del registro.
3. Actualizá el módulo o cargá los datos con *Actualizar lista de Apps*.

Forzar la herencia en productos existentes
-----------------------------------------
En *Odoo Shell* ejecutá:
```python
env["product.template"].search([])._onchange_categ_id_set_internal_tax()



y tambien tiene algunas traducciones que ha pedido el cliente
