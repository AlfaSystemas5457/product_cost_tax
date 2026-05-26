# Costo con Impuestos Incluidos

Muestra el costo con impuestos incluidos en la ficha del producto.

## Características

- Agrega un campo calculado `cost_tax_string` en `product.template` y `product.product`
- Muestra el costo + impuestos de compra en formato legible: `(= $116.00 Impuestos Incluidos)`
- Aparece automáticamente junto al campo "Impuestos de compra" en la vista de producto
- Compatible con empresas multicompañía (filtra impuestos por compañía)

## Dependencias

- `product`
- `account`

## Uso

1. Instale el módulo
2. Vaya a Ventas > Productos > Productos
3. Abra cualquier producto
4. En la pestaña "Información general", bajo "Costo", verá el texto con los impuestos incluidos
