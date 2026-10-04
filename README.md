# Loan Tracker Telegram Bot

A personal/family Telegram bot for tracking gold-loan payments using Python.

## Architecture

Telegram → Python Bot → Validation → Database → Google Sheets / Reports

OpenRouter AI will be added as a natural-language parsing layer. AI extracts structured payment information; financial calculations and database writes remain deterministic Python logic.

## Development Phases

1. Telegram bot foundation
2. Loan and payment data model
3. Payment tracking commands
4. Google Sheets export/sync
5. OpenRouter structured message parsing
6. Natural-language status/report queries
7. Production deployment (Render + PostgreSQL)

## Example

Message: `Paid Rs.1500 - SBI`

Expected structured data:

- Loan: SBI
- Amount: ₹1,500
- Type: payment/interest (confirmed by rules or user)
- Date: message date

## Security

- Never commit `.env` files, API keys, Telegram bot tokens, Google service-account credentials, or personal loan statements.
- AI is not the source of truth for balances. Python/database logic performs financial calculations.
