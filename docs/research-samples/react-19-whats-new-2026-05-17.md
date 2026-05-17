# Research sample: what is new in React 19

Date checked: 2026-05-17

## Question

What changed in React 19 that matters for a new SaaS MVP?

## Short answer

React 19 is stable and is worth using for a new React/Next.js MVP if the chosen
framework version supports it. The most useful changes for product work are
Actions for async mutations, form-related APIs, optimistic UI support, the new
`use` API for reading resources during render, better document/resource handling,
and simpler refs.

For an existing app, upgrade more carefully: React 19 removes several deprecated
APIs, requires the modern JSX transform, changes some TypeScript types, and can
surface issues in tests or libraries that depend on React internals.

## What changed

| Area | What React 19 adds or changes | MVP implication |
| --- | --- | --- |
| Async mutations | Actions let async functions in transitions manage pending state, errors, forms, and optimistic updates. | Less custom boilerplate for submit/update flows. |
| Forms | `form` actions, `useActionState`, and `useFormStatus` support form submissions and pending states. | Faster implementation of create/update forms and design-system buttons. |
| Optimistic UI | `useOptimistic` renders temporary optimistic state while an Action is pending. | Better UX for likes, carts, comments, and settings changes. |
| Resource reading | The `use` API can read promises and Context during render, with Suspense integration. | Useful when the framework/library provides cached Suspense-compatible resources. |
| Server Components | React 19 includes React Server Components features from the Canary channel for frameworks that support the full-stack architecture. | Use through a framework such as Next.js; do not build custom RSC infrastructure for an MVP. |
| Refs | Function components can receive `ref` as a prop; future React versions plan to deprecate `forwardRef`. | New components can be simpler, but existing code may wait for framework/library patterns. |
| Metadata/resources | Native support for document metadata, stylesheets, async scripts, and resource preloading APIs. | Better SSR/streaming integration and fewer ad hoc head/resource hacks. |
| Debugging | Improved hydration mismatch messages and error handling. | Easier SSR debugging for Next.js-style apps. |

## Facts and sources

- React 19 was released as stable on 2024-12-05. The official release post
  lists Actions, `useActionState`, form Actions, `useFormStatus`,
  `useOptimistic`, `use`, React DOM static APIs, Server Components, ref as a
  prop, hydration error diffs, metadata, stylesheets, async scripts, and
  resource preloading.
  Source: <https://react.dev/blog/2024/12/05/react-19>
- The React 19 upgrade guide says the modern JSX transform is required, suggests
  upgrading to React 18.3 first for warnings, and provides codemods for common
  migrations.
  Source: <https://react.dev/blog/2024/04/25/react-19-upgrade-guide>
- The upgrade guide lists removed/deprecated APIs including `ReactDOM.render`,
  `ReactDOM.hydrate`, `unmountComponentAtNode`, `findDOMNode`, string refs,
  legacy context, function-component `propTypes` checks/defaultProps, and
  `react-dom/test-utils` APIs other than `act`.
  Source: <https://react.dev/blog/2024/04/25/react-19-upgrade-guide>
- `useActionState` returns state, a dispatch Action, and an `isPending` flag for
  Action state. Its reducer action can be async and perform side effects.
  Source: <https://react.dev/reference/react/useActionState>
- `useOptimistic` lets a component show temporary optimistic state while an
  Action is in progress, then converge back to the canonical value.
  Source: <https://react.dev/reference/react/useOptimistic>

## Recommendation by scenario

- **New Next.js/React MVP:** use React 19 if the selected Next.js version,
  starter kit, component library, and test tooling support it.
- **Existing React 18 app:** upgrade to React 18.3 first, run React 19 codemods,
  then test forms, refs, hydration, and error reporting.
- **Heavy form/mutation product:** prioritize learning Actions,
  `useActionState`, `useFormStatus`, and `useOptimistic`.
- **Custom framework/RSC work:** avoid for MVP unless the team already owns a
  framework integration; use React Server Components through an established
  framework.

## Implications for StartupFamTeam

- For a greenfield SaaS prototype, React 19 can reduce boilerplate around
  pending states and optimistic updates.
- If the stack is Next.js, verify React 19 compatibility through the exact
  Next.js version and starter template before locking dependencies.
- Avoid legacy React patterns in new code: `ReactDOM.render`, string refs,
  `findDOMNode`, function `defaultProps`, and shallow renderer dependencies.
- When estimating implementation risk, check UI libraries and test setup first;
  those are more likely to block adoption than React app code written recently.

## Limits / unknowns

- This sample does not verify compatibility for a specific Next.js version,
  hosting provider, design system, or test runner.
- It does not cover React 19.2 changes; it focuses on the React 19 stable
  release and upgrade impact.

Confidence: high

Why: based on official React release, upgrade, and API documentation.

What would improve confidence: checking the exact app framework, package list,
and test tooling used by the target project.
