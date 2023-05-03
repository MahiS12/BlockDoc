<!-- PROJECT LOGO -->

  <h3 aling="center">BlockDoc: A Secure and Efficient Document Verification System</h3>

Ensuring the authenticity of documents and identities is a critical aspect of the recruitment process, not only for corporations but also for the education sector. However, the current document verification process in India is often time-consuming and does not guarantee authenticity. Fraudulent activities, such as submitting fake or manipulated documents, are not uncommon, leading to a lack of integrity in the education system. Motivated by the aspect of trying to improve the quality of the document verification process, hence leading towards the development of the integrity of the education system, while also streamlining and speeding up the conventional process, this paper discusses a Student Document Verification System that makes use of Digital Image Processing and Blockchain Technology. The system uses Optical Character Recognition to extract data from images, generating a hash value that is compared with the hash value on the blockchain to verify document authenticity and detect fraudulent documents. The results and observations obtained highlight the potential benefits of this proposed system in streamlining and speeding up the verification process while maintaining its accuracy and reliability.

## Features

- Secure document verification using Image Processing and Blockchain
- Fast and easy verification process, withour using intermediate services or third-party services
- User-friendly interface for document upload, verification, fetching and invalidation

## Usage

1. The owner of the system must first add an exporter to the list of authorized parties. This is done by clicking on the "Add Exporter" button and entering the exporter's Ethereum address.
2. Upload a document to the system by clicking on the "Upload Document" button and selecting a file from your computer. The document will be encrypted and stored in the IPFS network, and its hash will be recorded in the Blockchain.

3. Verify a document by clicking on the "Verify Document" button and entering its unique identifier (hash) in the input field. The system will retrieve the document from the IPFS network, decrypt it, and compare its hash with the one recorded in the Blockchain.

4. The system will display a message indicating whether the document is authentic or not.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments
- Metamask documentation
- Solidity and Web3.js documentation
- IPFS documentation
- Truffle documentation




