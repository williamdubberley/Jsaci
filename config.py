prefix = 'JASCI'
date_time_format = "%Y%m%d%H%M%S"
local_file_dir = 'd:/sftp_test'
companies = [
    {'company': 'Medifast',
     'host': '129.146.107.172',
     'username': 'sftpfossuser',
     'private_key': 'D:/wallets/WDTF',
     'tasks': [
         {'type': 'dev',
          'job_number': 1,
          'base_directory': 'sftpfossuser/medifast-edh-sftp/Sources/DOMO/dev1/FTW',
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
          'job_number': 2,
          'base_directory': 'sftpfossuser/medifast-edh-sftp/Sources/DOMO/prod/FTW',
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
