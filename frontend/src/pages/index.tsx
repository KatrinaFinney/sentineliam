import Link from "next/link";

export default function Home() {
  return (
    <main className="p-6 space-y-4">
      <h1 className="text-2xl font-bold">🛡 SentinelIAM</h1>
      <ul className="space-y-2">
        <li>
          <Link href="/audit" className="text-blue-500 hover:underline">
            📘 View Audit Logs
          </Link>
        </li>
        <li>
          <Link href="/templates" className="text-blue-500 hover:underline">
            📄 Browse Policy Templates
          </Link>
        </li>
      </ul>
    </main>
  );
}
