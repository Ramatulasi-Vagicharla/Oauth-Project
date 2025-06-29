// src/integrations/SlackIntegration.js

import { Button } from '@mui/material';
import { useEffect } from 'react';
import { authorize, getCredentials } from './slack';

export const SlackIntegration = ({ user, org, setIntegrationParams }) => {
  useEffect(() => {
    // Any startup logic can go here
  }, []);

  const handleConnect = async () => {
    await authorize(user, org);
  };

  const handleCredentials = async () => {
    const creds = await getCredentials(user, org);
    setIntegrationParams({
      type: 'slack',
      credentials: creds,
    });
  };

  return (
    <div>
      <Button variant="contained" onClick={handleConnect}>Authorize Slack</Button>
      <Button variant="outlined" onClick={handleCredentials} sx={{ ml: 2 }}>
        Get Credentials
      </Button>
    </div>
  );
};
