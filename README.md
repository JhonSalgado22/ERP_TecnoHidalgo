# Proyecto Final - ERP Open Source: TecnoHidalgo Comercial

## 1. Arranque con Docker
Requisitos: Docker Desktop.

Desde PowerShell, dentro de esta carpeta:
```powershell
docker compose up -d
```

Después abre:
http://localhost:8069

Crear base:
- Nombre: tecnohidalgo
- Email: admin@tecnohidalgo.mx
- Password: admin123
- No instalar datos de demostración.

La arquitectura usa dos contenedores:
- tecnohidalgo-odoo
- tecnohidalgo-db (PostgreSQL)

## 2. Módulos
Instalar CRM, Sales, Purchase, Inventory, Accounting/Invoicing y Website.

## 3. Datos listos
- productos.csv = 20 productos
- proveedores.csv = 5 proveedores
- clientes.csv = 10 clientes
- leads_crm.csv = 10 oportunidades
- ventas.csv = 10 operaciones de referencia
- compras.csv = 10 operaciones de referencia
- cuentas_contables.csv = 5 cuentas guía

Primero importa clientes, proveedores y productos. Después crea las órdenes de venta/compra en sus módulos usando los datos de los CSV; así quedan correctamente relacionadas y sirven para los reportes.

## 4. Landing Page
Instala la app "TecnoHidalgo Landing". Después:
http://localhost:8069/tecnohidalgo

## 5. Comandos útiles
Parar:
docker compose stop

Iniciar:
docker compose start

Ver estado:
docker compose ps

Ver logs:
docker compose logs -f web

Parar y eliminar contenedores sin borrar volúmenes:
docker compose down

NO uses `docker compose down -v` después de cargar datos, porque elimina los volúmenes y con ellos la información de la práctica.

## 6. Evidencias
Guardar capturas de:
Docker, inicio de Odoo, CRM, Inventario, Ventas, Compras, Proveedores, Contabilidad, Landing y los 3 reportes.
