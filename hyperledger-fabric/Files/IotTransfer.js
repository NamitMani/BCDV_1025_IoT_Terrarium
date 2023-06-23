"use strict";

const fs = require("fs");
const path = require("path");
const { Wallets, Gateway } = require("fabric-network");

const testNetworkRoot = path.resolve(
  require("os").homedir(),
  "fabric-samples/test-network"
);

async function main() {
  const gateway = new Gateway();
  const wallet = await Wallets.newFileSystemWallet("./wallet");

  try {
    let args = process.argv.slice(2);

    const identityLabel = args[0];
    const functionName = args[1];
    const chaincodeArgs = args
      .slice(2)
      .map((arg) => (arg.startsWith("{") ? JSON.parse(arg) : arg));

    const orgName = identityLabel.split("@")[1];
    const orgNameWithoutDomain = orgName.split(".")[0];

    let connectionProfile = JSON.parse(
      fs.readFileSync(
        path.join(
          testNetworkRoot,
          "organizations/peerOrganizations",
          orgName,
          `/connection-${orgNameWithoutDomain}.json`
        ),
        "utf8"
      )
    );

    let connectionOptions = {
      identity: identityLabel,
      wallet: wallet,
      discovery: { enabled: true, asLocalhost: true },
    };

    console.log("Connect to a Hyperledger Fabric gateway.");
    await gateway.connect(connectionProfile, connectionOptions);

    console.log('Use channel "mychannel".');
    const network = await gateway.getNetwork("mychannel");

    console.log("Use TerrariumMonitor."); // corrected chaincode name
    const contract = network.getContract("terrarium_monitor"); // corrected chaincode name

    console.log("Submit " + functionName + " transaction.");
    const res = await contract.submitTransaction(
      functionName,
      ...chaincodeArgs
    );

    if (`${res}` !== "") {
      console.log(`Response from ${functionName}: ${res}`);
      var json = JSON.stringify(res.toString());
      console.log(json);
    } else {
      console.log("Transaction Submitted Successfully");
    }
  } catch (error) {
    console.log(`Error processing transaction. ${error}`);
    console.log(error.stack);
  } finally {
    console.log("Disconnect from the gateway.");
    gateway.disconnect();
  }
}

main().catch((e) => console.error(e));
