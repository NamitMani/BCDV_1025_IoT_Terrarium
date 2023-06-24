
# Terrarium IoT Blockchain Project:

## Team Members Roles
-  **NAMIT MANI** <br>
  **Student ID** #101383808 <br>
  **Roles:** Chaincode Developer <br>


- **ANIKET SRIVASTAVA** <br>
  **Student ID** #101469899 <br>
  **Roles:** Architect <br>


- **FAWAZ MALIK** <br>
  **Student ID** #101461582 <br>
  **Roles:** Business Analyst <br>


- **BADARUDDIN KHUHRO** <br>
  **Student ID** #101467663 <br>
  **Roles:** Lead Front End Developer <br>


- **HEMANTH KUMAR VARMA POTHURI** <br>
  **Student ID** #101464127 <br>
  **Roles:** co-Front End Developer + co-Business Analyst <br>


This project implements a blockchain solution using Hyperledger Fabric to facilitate secure and transparent purchase transactions between shop owners and customers in the terrarium IoT industry. The blockchain enables efficient communication, inventory management, and real-time monitoring of IoT devices.


## Requirements
**Features (Function)**

BuyPet (Pet Name, ID) <br>
BuyTank (Name, ID) <br>
SellTank (Tank Name, ID) <br>
SellPet (Pet Name, ID)  <br>
SetupTank (IoT device NAME, ID) <br>
Update Inventory (Item_ID, Item_Name) <br>
Sell IoT device( Device_Name, ID) <br>
Make IoT device ( Device_Name, ID) <br>
Make Tank ( Tank_Name, ID) <br> 
Provide service (Service_ID,) <br>

**Reasons**
1. Enhanced traceability of pets, tanks, and IoT devices.
2. Improved inventory management for shop owners and manufacturers.
3. Real-time monitoring and safety features for terrariums.
4. Streamlined buying and selling processes.
5. Creation of a secure and trusted environment for all participants.
6. Efficient supply chain management among manufacturers, shop owners, and customers.
7. Ensuring product quality and minimizing the risk of recalls.
8. Transparency in transactions and activities recorded on the blockchain.
9. Facilitating remote monitoring and control of terrariums.
10. Leveraging blockchain technology for improved efficiency and customer satisfaction.


## Business Use Case

The primary objective of this blockchain implementation is to enhance the purchase transaction process between shop owners and customers in the terrarium IoT industry. The project offers the following features:

1. Secure Purchase Transactions:
   - Customers can securely purchase pets and terrarium tanks from shop owners using the blockchain.
   - Transaction details are recorded on the Hyperledger Fabric blockchain, ensuring data integrity and security.

2. Transparent Transactions:
   - All transaction details, including purchase information and payment records, are stored on the blockchain.
   - Both shop owners and customers can access and verify the transaction history, promoting transparency and trust.

3. Efficient Communication:
   - The blockchain facilitates seamless communication between shop owners, customers, and IoT device manufacturers.
   - Shop owners can place orders with manufacturers, track the status of their orders, and receive updates through the blockchain network.

4. Inventory Management:
   - Shop owners' inventories are managed and updated on the blockchain.
   - When a terrarium tank and pet are sold, the inventory is automatically adjusted to reflect the availability of products.

5. Real-time Monitoring of IoT Devices:
   - Each terrarium tank sold includes an IoT device for health and safety monitoring.
   - Customers can test the IoT device at the shop using the "Start tank" button on the front-end application, initiating real-time data collection and monitoring.

The project workflow had following implementations:
-3 organizations: Manufacturer, PetOwner, Shopowner
-1 Channel: 1 channel named mychannel

## User Roles

1. Shop Owners:
   - Shop owners can access the blockchain network to place orders with IoT device manufacturers.
   - They can view and manage their inventory on the blockchain.
   - Shop owners can initiate purchase transactions with customers and record the details on the blockchain.

2. Pet Owners (Customers):
   - Customers can securely purchase pets and terrarium tanks from shop owners using the blockchain.
   - They can verify the authenticity of the transaction and access the transaction history on the blockchain.

3. Small IoT Device Manufacturers:
   - IoT device manufacturers can participate in the blockchain network to receive orders from shop owners.
   - They can update the status of orders and communicate with shop owners through the blockchain.

## Purchase Transaction Process

1. Shop owners list available terrarium tanks and pets with IoT devices on the blockchain platform.
2. Customers browse the available options and select the desired terrarium tank and pet.
3. The customer initiates the purchase transaction by clicking the "Buy" button on the front-end application.
4. The transaction details, including the purchased items, payment information, and customer details, are securely recorded on the Hyperledger Fabric blockchain.
5. The shop owner confirms the transaction and prepares the terrarium tank and pet with the associated IoT device.
6. At the shop, the customer can test the IoT device by clicking the "Start tank" button on the front-end application.
7. Real-time data from the IoT device is collected and stored on the blockchain, providing health and safety monitoring for the pet.
8. Both the shop owner and customer can access the transaction details and IoT device data on the blockchain, ensuring transparency and trust.


## Project Components

The project consists of the following components:

1. Front-end Application:
   - Provides a user-friendly interface for shop owners and customers to interact with the blockchain network.
   - Enables customers to browse and select terrarium tanks and pets, initiate purchase transactions, and monitor IoT device data.

2. Smart Contracts:
   - Define the business logic and rules for purchase transactions and inventory management.
   - Manage permissions and access control for shop owners, customers, and IoT device manufacturers.
   - Record transaction details and IoT device data on the Hyperledger Fabric blockchain.

3. Blockchain Network:
   - Implements the Hyperledger Fabric blockchain framework for secure and decentralized transaction processing.
   - Ensures data integrity, immutability, and transparency of all transactions and data recorded on the blockchain.

4. IoT Device Integration:
   - Integrate IoT devices with the blockchain network to enable real-time monitoring and data collection.
   - Ensure the seamless transmission of IoT device data to the blockchain for storage and analysis.

## Conclusion

The terrarium IoT blockchain project leverages Hyperledger Fabric to streamline purchase transactions, enhance inventory management, and enable real-time monitoring of IoT devices. By providing secure and transparent transactions, the project aims to improve the overall customer experience and promote trust in the terrarium IoT industry.




## SNAPSHOTS OF THE PROJECT
1. API AND POSTMAN REQUESTS
![API and POSTMAN REQUEST](https://github.com/NamitMani/BCDV_1025_IoT_Terrarium/assets/90002484/a80d0af5-b01a-4903-9955-7c6f251d7089)
  
2. REPONSE RECIEVED BY THE BLOCKCHAIN
![Application - Part 2 - Blockchain receives response](https://github.com/NamitMani/BCDV_1025_IoT_Terrarium/assets/90002484/c942ae3d-0749-4934-a160-ad186fa1b33f)
