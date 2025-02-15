# [[Class Notes]](https://github.com/hirusha-adi/Classs-Notes) Data

For [server-vps-class](https://github.com/hirusha-adi/server-vps-class).

## Folder Structure

All directories in this repository should be placed inside the `pb_public` folder.

The system assumes your PocketBase installation's data is located at:  
`/srv/hirusha-class-notes/pocketbase/pb_public`  

⚠️ **Warning:** Everything inside the `pb_public` folder will be deleted and replaced during the setup process.

## Usage

To deploy the data, run the provided Python script on the server:

```bash
python3 copy_files.sh
```

## Important Notes

- **Do not edit any files inside the `pb_public` folder.**

By following these instructions, you can ensure proper synchronization of the data for the Class Notes app.
