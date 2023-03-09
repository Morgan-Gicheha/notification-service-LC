module.exports = {
  apps: [{
    name: 'API:NOTIFICATIONS:WORKER',
    script: 'python3 tools/rabbitMQ/bootWorker.py',
    instances: '1',
    // exec_mode: 'cluster',
    watch: false,
    error_file: './log/err.log',
    out_file: './log/out.log',
    log_file: './log/combined.log',
    time: true,
  },

  ],

};
