export function toast({ title, description, variant }: { title: string; description: string; variant?: string }) {
  // This is a simplified version - in a real app, you'd use a proper toast library
  console.log(`Toast: ${title} - ${description}`)
}
