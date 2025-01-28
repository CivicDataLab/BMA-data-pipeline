# BMA CLI Tool Documentation

A command-line interface tool for managing the BMA Django application.

## Installation

```bash
# Install the package in development mode
pip install -e .
```

## Available Commands

### `bma start`
Starts the Django development server.

```bash
# Start server on default port (8080)
bma start

# Start server on custom port
bma start --port 8000
```

**Options:**
- `-p, --port INTEGER`: Port to run server on [default: 8000]
- `--help`: Show command help message

### `bma migrate`
Run Django database migrations.

```bash
bma migrate
```

**Options:**
- `--help`: Show command help message

### `bma shell`
Open Django interactive shell.

```bash
bma shell
```

**Options:**
- `--help`: Show command help message

## Global Options

These options are available for all commands:

### Shell Completion
```bash
# Install shell completion
bma --install-completion [bash|zsh|fish|powershell|pwsh]

# Show completion script
bma --show-completion [bash|zsh|fish|powershell|pwsh]
```

### Help
```bash
# Show general help
bma --help

# Show command-specific help
bma <command> --help
```

## Examples

```bash
# Start server on port 9000
bma start -p 9000

# Run migrations and then start server
bma migrate && bma start

# Get help for start command
bma start --help
```