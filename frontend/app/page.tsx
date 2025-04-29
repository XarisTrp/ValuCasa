import { HouseFeatureForm } from "@/components/house-feature-form"

export default function Home() {
  return (
    <main className="min-h-screen bg-slate-100 dark:bg-slate-900 py-12 px-4">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-3xl font-bold mb-2 text-center text-slate-800 dark:text-slate-100">Valu Casa</h1>
        <p className="text-slate-600 dark:text-slate-400 text-center mb-8">Enter property details to get started</p>
        <HouseFeatureForm />
      </div>
    </main>
  )
}
