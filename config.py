prefix = 'JASCI'
date_time_format = "%Y%m%d%H%M%S"
local_file_dir = '/home/tomcat/sftp'
companies = [
    {'company': 'Medifast',
     'host': 'edhsftp.medifastinc.com',
     'tasks': [
         {'type': 'dev',
          'job_number': 2,
          'username': 'jasci_dev_mwint',
          'private_key': '/home/tomcat/.ssh/Privatekey_JASCI_DEV.key',
          'base_directory': '/medifast-edh-sftp',
          'integrations': [
              {
                  'name': 'ShipSummary',
                  'folder': 'Sources/Shipment_ETL/',
              },
              {
                  'name': 'TransferOrder_Receipts',
                  'folder': 'Sources/DOMO/dev1/FTW/TransferOrderReceipts/',
              },
              {
                  'name': 'InventoryAdjustments',
                  'folder': 'Sources/DOMO/dev1/FTW/InventoryAdj/',
              },
              {
                  'name': 'PurchaseOrder_Receipts',
                  'folder': 'Sources/DOMO/dev1/FTW/PurchaseOrderReceipts/',
              },
              {
                  'name': 'TransferOrder_Shipments',
                  'folder': 'Sources/DOMO/dev1/FTW/TransferOrderShipments/',
              },
              {
                  'name': 'RMA_Receipts',
                  'folder': 'Sources/DOMO/dev1/FTW/RMAReceiptConf/',
              }
          ]
          },
         {'type': 'prod',
          'job_number': 3,
          'username': 'jasci_prod_mwint',
          'private_key': '/home/tomcat/.ssh/privatekey_jasciv2.key',
          'base_directory': '/medifast-edh-sftp-prod/Sources',
          'integrations': [
              {
                  'name': 'InventoryAdjustments',
                  'folder': 'DOMO/prod/FTW/InventoryAdj/',
              },
              {
                  'name': 'PurchaseOrder_Receipts',
                  'folder': 'DOMO/prod/FTW/PurchaseOrderReceipts/',
              },
              {
                  'name': 'RMA_Receipts',
                  'folder': 'DOMO/prod/FTW/RMAReceiptConf/',
              },
              {
                  'name': 'TransferOrder_Receipts',
                  'folder': 'DOMO/prod/FTW/TransferOrderReceipts/',
              },
              {
                  'name': 'TransferOrder_Shipments',
                  'folder': 'DOMO/prod/FTW/TransferOrderShipments/',
              },
              {
                  'name': 'ShipSummary',
                  'folder': 'Shipment_ETL/ShipSummary/',
              }
          ]
          }
     ]
     },
   {'company': 'medifast2',
     'host': '',
     'username': '',
     'password': '',
     'tasks': [
         {'type': 'dev',
          'job_number': 3,
          'base_directory': 'sftpfossuser/medifast2-edh-sftp/Sources/DOMO/dev1/FTW',
          'integrations': [
              {
                  'name': 'InventoryAdjustments',
                  'folder': 'InventoryAdj',
              },
              {
                  'name': 'PurchaseOrder_Receipts',
                  'folder': 'PurchaseOrderReceipts',
              },
              {
                  'name': 'RMA_Receipts',
                  'folder': 'RMAReceiptConf',
              },
              {
                  'name': 'TransferOrder_Receipts',
                  'folder': 'TransferOrderReceipts',
              },
              {
                  'name': 'TransferOrder_Shipments',
                  'folder': 'TransferOrderShipments',
              }
          ]
          },
         {'type': 'prod',
          'job_number': 4,
          'base_directory': 'sftpfossuser/medifast2-edh-sftp/Sources/DOMO/prod/FTW',
          'integrations': [
              {
                  'name': 'InventoryAdjustments',
                  'folder': 'InventoryAdj',
              },
              {
                  'name': 'PurchaseOrder_Receipts',
                  'folder': 'PurchaseOrderReceipts',
              },
              {
                  'name': 'RMA_Receipts',
                  'folder': 'RMAReceiptConf',
              },
              {
                  'name': 'TransferOrder_Receipts',
                  'folder': 'TransferOrderReceipts',
              },
              {
                  'name': 'TransferOrder_Shipments',
                  'folder': 'TransferOrderShipments',
              }
]
          }
     ]
     }
]
