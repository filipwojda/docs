# regards.design docs

The public docs for the regards.design MCP server, on [Mintlify](https://mintlify.com): what it indexes, how to
connect each client, Instant and Deep, the tools and example prompts. Everything in them is taken from the app's
code (the `aggregator` repo): `src/lib/server/mcp/server.ts` for the tools, `src/lib/agents/clients.ts` for the
clients, `src/lib/billing/plans.ts` and the guard's limits for plans. Change them together.

| page | |
| --- | --- |
| `index.mdx` | Overview |
| `connect.mdx` | Connect your agent |
| `deep.mdx` | Instant and Deep, plans and limits |
| `tools.mdx` | The five tools, their parameters, coordinates |
| `examples.mdx` | Example prompts |

Our name in body copy goes through `<Regards domain />` (`snippets/regards.jsx`), the mark before the word as
the site draws it; titles, URLs and code stay plain. `logo/light.svg` and `logo/dark.svg` are drawn by
`scripts/lockup.py` from the app's `static/logo/mark-small.svg` and Public Sans.

## Preview

```
npx mint dev
npx mint broken-links
```

## Publish

Mintlify deploys the branch its GitHub app watches (main) on every push.
