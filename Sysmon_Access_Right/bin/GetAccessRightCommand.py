import sys
from splunklib.searchcommands import dispatch, StreamingCommand, Configuration

def get_access_right(granted_access):
    process_permissions = {
        "PROCESS_CREATE_PROCESS": 0x0080,
        "PROCESS_CREATE_THREAD": 0x0002,
        "PROCESS_DUP_HANDLE": 0x0040,
        "PROCESS_SET_INFORMATION": 0x0200,
        "PROCESS_SET_QUOTA": 0x0100,
        "PROCESS_QUERY_LIMITED_INFORMATION": 0x1000,
        "PROCESS_QUERY_INFORMATION": 0x0400,
        "PROCESS_SUSPEND_RESUME": 0x0800,
        "PROCESS_TERMINATE": 0x0001,
        "PROCESS_VM_OPERATION": 0x0008,
        "PROCESS_VM_READ": 0x0010,
        "PROCESS_VM_WRITE": 0x0020,
        "SYNCHRONIZE": 0x00100000
    }

    access_rights = []
    for access, value in process_permissions.items():
        if granted_access & value:
            access_rights.append(access)

    return access_rights

@Configuration()
class GetAccessRightCommand(StreamingCommand):
    def stream(self, records):
        for record in records:
            input_field = self.fieldnames[0] # Get the input field name directly from the first field
            if input_field in record and record[input_field]:  # Ensure the field is present and not empty
                try:
                    access_value = int(record[input_field], 0)
                    access_rights = get_access_right(access_value)
                    record['AccessRights'] = access_rights # Add AccessRights field containing access rights
                except ValueError:
                    record['AccessRights'] = 'Invalid access value'
            else:
                record['AccessRights'] = 'Missing or empty access value'
            yield record

if __name__ == "__main__":
    dispatch(GetAccessRightCommand, sys.argv, sys.stdin, sys.stdout, __name__)
