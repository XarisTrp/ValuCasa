"use client"

import { useState } from "react"
import { zodResolver } from "@hookform/resolvers/zod"
import { useForm } from "react-hook-form"
import * as z from "zod"
import { Loader2, Home, MapPin, Layers, Bath, Coffee, Sofa, Check, ChevronsUpDown } from "lucide-react"


import { Button } from "@/components/ui/button"
import { Form, FormControl, FormDescription, FormField, FormItem, FormLabel, FormMessage } from "@/components/ui/form"
import { Input } from "@/components/ui/input"
import { toast } from "@/components/ui/use-toast"
import { Card, CardContent, CardDescription, CardHeader, CardTitle, CardFooter } from "@/components/ui/card"
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert"
import { Command, CommandEmpty, CommandGroup, CommandInput, CommandItem, CommandList } from "@/components/ui/command"
import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover"
import { Separator } from "@/components/ui/separator"


const formSchema = z.object({
  sq_meters: z.coerce.number().positive({
    message: "Surface area must be a positive number",
  }),
  geography: z.string().min(1, {
    message: "Geographical area is required",
  }),
  floorNumber: z.coerce.number().int({
    message: "Floor number must be an integer",
  }),
  rooms: z.coerce.number().int().nonnegative({
    message: "Number of rooms must be a non-negative integer",
  }),
  no_of_bathrooms: z.coerce.number().int().nonnegative({
    message: "Number of bathrooms must be a non-negative integer",
  }),
  kitchens: z.coerce.number().int().nonnegative({
    message: "Number of kitchens must be a non-negative integer",
  }),
  livingRooms: z.coerce.number().int().nonnegative({
    message: "Number of living rooms must be a non-negative integer",
  }),
})

// Geographical areas for dropdown
const geographicalAreas = ['A Nekrotafeio (Athens - Center)',
  'Ag. Meletiou - Viktorias Sq. - Marni (Athens - Center)',
  'Agios Artemios (Athens - Center)',
  'Agios Eleftherios (Athens - Center)',
  'Agios Eleftherios - Probona - Rizoupoli (Athens - Center)',
  'Agios Ioannis (Athens - Center)',
  'Agios Nikolaos (Athens - Center)',
  'Agios Panteleimonas (Athens - Center)',
  'Agios Sostis (Athens - Center)', 'Agios Thomas (Athens - Center)',
  'Akadimia (Athens - Center)', 'Akropoli (Athens - Center)',
  'Alsos (Athens - Center)', 'Alsos Pagkratiou (Athens - Center)',
  'Ampelokipoi (Athens - Center)',
  'Ampelokipoi - Pentagon (Athens - Center)',
  'Ano Kipseli - Evelpidon (Athens - Center)',
  'Ano Patisia (Athens - Center)', 'Ano Petralona (Athens - Center)',
  'Athens Medical School (Athens - Center)',
  'Attiki (Athens - Center)', 'Attiko Alsos (Athens - Center)',
  'Center (Athens - Center)', 'Elinoroson (Athens - Center)',
  'Erithros (Athens - Center)', 'Evelpidon (Athens - Center)',
  'Exarcheia (Athens - Center)',
  'Exarchia - Neapoli (Athens - Center)',
  'Filopapou (Athens - Center)', 'Fix (Koukaki - Makrygianni)',
  'Fokionos Negri (Athens - Center)',
  'Gazi - Metaxourgio - Votanikos (Athens - Center)',
  'Girokomeio (Athens - Center)',
  'Gizi - Pedion Areos (Athens - Center)', 'Gkazi (Athens - Center)',
  'Gkrava (Athens - Center)',
  'Gkyzi - Arios Pagos (Athens - Center)', 'Goudi (Athens - Center)',
  'Hilton (Athens - Center)', 'Historic Center (Athens - Center)',
  'Ilisia (Athens - Center)', 'Kallimarmaro (Athens - Center)',
  'Kato Ilisia (Athens - Center)', 'Kato Patisia (Athens - Center)',
  'Kato Petralona (Athens - Center)', 'Kentro (Athens - Center)',
  'Kerameikos (Athens - Center)', 'Kinosargous (Athens - Center)',
  'Kipriadou - Ano Patisia (Athens - Center)',
  'Kipseli (Athens - Center)', 'Klonaridou (Athens - Center)',
  'Kolokinthous (Kolonos - Kolokynthous)',
  'Kolonaki (Kolonaki - Lykavittos)',
  'Kolonaki - Lykavittos (Athens - Center)',
  'Kolonos (Kolonos - Kolokynthous)',
  'Kolonos - Kolokynthous (Athens - Center)',
  'Koukaki - Makrygianni (Athens - Center)',
  'Koukaki - Pediki Chara (Koukaki - Makrygianni)',
  'Labrini (Athens - Center)', 'Leof. Liosion (Athens - Center)',
  'Likavittos (Kolonaki - Lykavittos)',
  'Lofos Finopoulou (Athens - Center)',
  'Lofos Skouze (Athens - Center)',
  'Makrigianni (Koukaki - Makrygianni)',
  'Metaxourgeio (Athens - Center)', 'Mets (Athens - Center)',
  'Mets - Kalimarmaro (Athens - Center)',
  'Monastiraki (Athens - Center)', 'Mouseio (Athens - Center)',
  'Nea Filothei (Athens - Center)', 'Nea Kipseli (Athens - Center)',
  'Neapoli Exarcheion (Athens - Center)',
  'Neos Kosmos (Athens - Center)',
  'Nosokomeio Pedon (Athens - Center)', 'Omonoia (Athens - Center)',
  'Osios Loukas (Athens - Center)', 'Pagkrati (Athens - Center)',
  'Pagkrati Center (Athens - Center)', 'Panormou (Athens - Center)',
  'Patisia (Athens - Center)',
  'Patision - Acharnon (Athens - Center)',
  'Pedion Areos (Athens - Center)', 'Pentagono (Athens - Center)',
  'Petralona (Athens - Center)', 'Plaka (Athens - Center)',
  'Plateia Amerikis (Athens - Center)',
  'Plateia Klafthmonos (Athens - Center)',
  'Plateia Koliatsou (Athens - Center)',
  'Plateia Mavili (Athens - Center)',
  'Plateia Vathis (Athens - Center)',
  'Platia Attikis (Athens - Center)',
  'Platia Gkizi (Athens - Center)',
  'Platia Kanigos (Athens - Center)',
  'Platia Karitsi (Athens - Center)',
  'Platia Kipselis (Athens - Center)',
  'Platia Koumoundourou (Athens - Center)',
  'Platia Papadiamanti (Athens - Center)',
  'Poligono (Athens - Center)',
  'Poligono - Tourkovounia (Athens - Center)',
  'Politechneio (Athens - Center)', 'Probona (Athens - Center)',
  'Profitis Ilias (Athens - Center)', 'Psirri (Athens - Center)',
  'Pyrgos Athinon (Athens - Center)',
  'Rigilis (Kolonaki - Lykavittos)', 'Rizoupoli (Athens - Center)',
  'Rouf (Athens - Center)', 'Sepolia (Athens - Center)',
  'Sepolia - Skouze (Athens - Center)', 'Sintagma (Athens - Center)',
  'Soutsou (Athens - Center)',
  'Stathmos Larisis (Kolonos - Kolokynthous)',
  'Thimarakia (Athens - Center)', 'Thiseio (Athens - Center)',
  'Tourkovounia (Athens - Center)',
  'Treis Gefires (Athens - Center)', 'Varnava (Athens - Center)',
  'Votanikos (Athens - Center)',
  'akadimia Platonos (Kolonos - Kolokynthous)']

type FormValues = z.infer<typeof formSchema>

// Define interface for geographical area
interface GeographicalArea {
  name: string
}

export function HouseFeatureForm() {
  const [isSubmitting, setIsSubmitting] = useState(false)
  const [submitSuccess, setSubmitSuccess] = useState(false)
  const [submitError, setSubmitError] = useState<string | null>(null)
  const [calculationResults, setCalculationResults] = useState<any>(null)

  setSubmitError
  const form = useForm<FormValues>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      sq_meters: 0,
      geography: "",
      floorNumber: 0,
      rooms: 0,
      no_of_bathrooms: 0,
      kitchens: 0,
      livingRooms: 0,
    },
  })

  async function onSubmit(data: FormValues) {
    setIsSubmitting(true)
    setSubmitSuccess(false)
    setSubmitError(null)
    setCalculationResults(null)

    try {

      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      })

      if (!response.ok) {
        throw new Error(`Error: ${response.status} - ${await response.text()}`)
      }

      const responseData = await response.json()

      console.log(responseData)
      setSubmitSuccess(true)
      // Store the calculation results from the backend
      if (responseData.predicted_price) {
        setCalculationResults(responseData.predicted_price)
      }

      form.reset()
      toast({
        title: "Success!",
        description: "House features have been submitted successfully.",
      })
    } catch (error) {
      console.error("Submission error:", error)
      setSubmitError(error instanceof Error ? error.message : "An unknown error occurred")
      toast({
        title: "Error",
        description: "Failed to submit house features. Please try again.",
        variant: "destructive",
      })
    } finally {
      setIsSubmitting(false)
    }
  }
  const formattedPredictedPrice = calculationResults
  ? Math.floor(calculationResults).toLocaleString()
  : null

  console.log(calculationResults)
  return (
    <Card className="border-0 shadow-lg bg-white/90 dark:bg-slate-800/90 backdrop-blur-sm">
      <CardHeader className="pb-4 border-b border-slate-100 dark:border-slate-700">
        <CardTitle className="text-2xl font-semibold text-slate-800 dark:text-slate-100">Property Details</CardTitle>
        <CardDescription className="text-slate-500 dark:text-slate-400">
          Enter the details of the property to submit to the database
        </CardDescription>
      </CardHeader>
      <CardContent className="pt-6">
        {submitSuccess && (
          <Alert className="mb-6 bg-emerald-50 dark:bg-emerald-900/20 border-emerald-200 dark:border-emerald-800 text-emerald-800 dark:text-emerald-300">
            <div className="flex items-center gap-2">
              <Check className="h-4 w-4" />
              <AlertTitle className="font-medium">Success!</AlertTitle>
            </div>
            <AlertDescription className="mt-1">Your house features have been submitted successfully.</AlertDescription>
          </Alert>
        )}

        {submitSuccess && calculationResults && (
          <div className="mt-6 mb-6">
            <Card>
              <CardHeader>
                <CardTitle className="text-xl text-slate-800 dark:text-slate-100">Calculation Results</CardTitle>
                <CardDescription>Results based on your property details</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="text-center py-4">
                  <div className="text-4xl font-bold text-emerald-600 dark:text-emerald-400">
                    €{formattedPredictedPrice}
                  </div>
                  <div className="text-sm text-slate-500 dark:text-slate-400 mt-2">Estimated market value</div>
                </div>
              </CardContent>
            </Card>
          </div>
        )}

        {submitError && (
          <Alert
            className="mb-6 bg-rose-50 dark:bg-rose-900/20 border-rose-200 dark:border-rose-800 text-rose-800 dark:text-rose-300"
            variant="destructive"
          >
            <AlertTitle className="font-medium">Submission Failed</AlertTitle>
            <AlertDescription className="mt-1">{submitError}</AlertDescription>
          </Alert>
        )}

        <Form {...form}>
          <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
            <div>
              <h3 className="text-lg font-medium text-slate-800 dark:text-slate-200 mb-4 flex items-center gap-2">
                <Home className="h-5 w-5 text-slate-600 dark:text-slate-400" />
                Basic Information
              </h3>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <FormField
                  control={form.control}
                  name="sq_meters"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel className="text-slate-700 dark:text-slate-300">Surface Area (m²)</FormLabel>
                      <FormControl>
                        <Input
                          type="number"
                          step="0.01"
                          placeholder="100.5"
                          {...field}
                          className="bg-slate-50 dark:bg-slate-700/50 border-slate-200 dark:border-slate-600 focus:border-slate-400 dark:focus:border-slate-500"
                        />
                      </FormControl>
                      <FormDescription className="text-slate-500 dark:text-slate-400">
                        Surface area in square meters
                      </FormDescription>
                      <FormMessage className="text-rose-500" />
                    </FormItem>
                  )}
                />

                <FormField
                  control={form.control}
                  name="geography"
                  render={({ field }) => (
                    <FormItem className="flex flex-col">
                      <FormLabel className="text-slate-700 dark:text-slate-300">Geographical Area</FormLabel>
                      <Popover>
                        <PopoverTrigger asChild>
                          <FormControl>
                            <div
                              className={`flex h-10 w-full items-center justify-between rounded-md border border-slate-200 dark:border-slate-600 bg-slate-50 dark:bg-slate-700/50 px-3 py-2 text-sm ring-offset-background placeholder:text-slate-400 dark:placeholder:text-slate-500 focus:outline-none focus:ring-2 focus:ring-slate-400 dark:focus:ring-slate-500 focus:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 ${
                                !field.value && "text-slate-400 dark:text-slate-500"
                              }`}
                              role="combobox"
                              aria-expanded="false"
                              tabIndex={0}
                            >
                              <div className="flex items-center gap-2">
                                <MapPin className="h-4 w-4 text-slate-500 dark:text-slate-400" />
                                {field.value
                                  ? geographicalAreas.find(
                                      (area) => area.toLowerCase() === field.value.toLowerCase(),
                                    ) || field.value
                                  : "Select location..."}
                              </div>
                              <ChevronsUpDown className="ml-2 h-4 w-4 shrink-0 opacity-50" />
                            </div>
                          </FormControl>
                        </PopoverTrigger>
                        <PopoverContent className="w-full p-0 bg-white dark:bg-slate-800 border-slate-200 dark:border-slate-700">
                          <Command className="bg-transparent">
                            <CommandInput placeholder="Search location..." className="border-none focus:ring-0" />
                            <CommandList>
                              <CommandEmpty className="py-3 text-center text-sm text-slate-500 dark:text-slate-400">
                                No location found.
                              </CommandEmpty>
                              <CommandGroup className="max-h-60 overflow-y-auto">
                                {geographicalAreas.map((area: string) => (
                                  <CommandItem
                                    key={area}
                                    value={area}
                                    onSelect={() => {
                                      form.setValue("geography", area, { shouldValidate: true })
                                    }}
                                    className="flex items-center gap-2 px-4 py-2 hover:bg-slate-100 dark:hover:bg-slate-700 aria-selected:bg-slate-100 dark:aria-selected:bg-slate-700"
                                  >
                                    <Check
                                      className={`mr-2 h-4 w-4 text-emerald-500 ${
                                        field.value?.toLowerCase() === area.toLowerCase() ? "opacity-100" : "opacity-0"
                                      }`}
                                    />
                                    {area}
                                  </CommandItem>
                                ))}
                              </CommandGroup>
                            </CommandList>
                          </Command>
                        </PopoverContent>
                      </Popover>
                      <FormDescription className="text-slate-500 dark:text-slate-400">
                        City, neighborhood, or area
                      </FormDescription>
                      <FormMessage className="text-rose-500" />
                    </FormItem>
                  )}
                />

                <FormField
                  control={form.control}
                  name="floorNumber"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel className="text-slate-700 dark:text-slate-300">Floor Number</FormLabel>
                      <FormControl>
                        <Input
                          type="number"
                          placeholder="2"
                          {...field}
                          className="bg-slate-50 dark:bg-slate-700/50 border-slate-200 dark:border-slate-600 focus:border-slate-400 dark:focus:border-slate-500"
                        />
                      </FormControl>
                      <FormDescription className="text-slate-500 dark:text-slate-400">
                        Floor number of the property
                      </FormDescription>
                      <FormMessage className="text-rose-500" />
                    </FormItem>
                  )}
                />
              </div>
            </div>

            <Separator className="my-6 bg-slate-200 dark:bg-slate-700" />

            <div>
              <h3 className="text-lg font-medium text-slate-800 dark:text-slate-200 mb-4 flex items-center gap-2">
                <Layers className="h-5 w-5 text-slate-600 dark:text-slate-400" />
                Room Information
              </h3>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <FormField
                  control={form.control}
                  name="rooms"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel className="text-slate-700 dark:text-slate-300">Number of Rooms</FormLabel>
                      <FormControl>
                        <Input
                          type="number"
                          placeholder="3"
                          {...field}
                          className="bg-slate-50 dark:bg-slate-700/50 border-slate-200 dark:border-slate-600 focus:border-slate-400 dark:focus:border-slate-500"
                        />
                      </FormControl>
                      <FormDescription className="text-slate-500 dark:text-slate-400">
                        Total number of rooms
                      </FormDescription>
                      <FormMessage className="text-rose-500" />
                    </FormItem>
                  )}
                />

                <FormField
                  control={form.control}
                  name="no_of_bathrooms"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel className="text-slate-700 dark:text-slate-300">
                        <div className="flex items-center gap-2">
                          <Bath className="h-4 w-4 text-slate-500 dark:text-slate-400" />
                          Number of Bathrooms
                        </div>
                      </FormLabel>
                      <FormControl>
                        <Input
                          type="number"
                          placeholder="2"
                          {...field}
                          className="bg-slate-50 dark:bg-slate-700/50 border-slate-200 dark:border-slate-600 focus:border-slate-400 dark:focus:border-slate-500"
                        />
                      </FormControl>
                      <FormDescription className="text-slate-500 dark:text-slate-400">
                        Total number of bathrooms
                      </FormDescription>
                      <FormMessage className="text-rose-500" />
                    </FormItem>
                  )}
                />

                <FormField
                  control={form.control}
                  name="kitchens"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel className="text-slate-700 dark:text-slate-300">
                        <div className="flex items-center gap-2">
                          <Coffee className="h-4 w-4 text-slate-500 dark:text-slate-400" />
                          Number of Kitchens
                        </div>
                      </FormLabel>
                      <FormControl>
                        <Input
                          type="number"
                          placeholder="1"
                          {...field}
                          className="bg-slate-50 dark:bg-slate-700/50 border-slate-200 dark:border-slate-600 focus:border-slate-400 dark:focus:border-slate-500"
                        />
                      </FormControl>
                      <FormDescription className="text-slate-500 dark:text-slate-400">
                        Total number of kitchens
                      </FormDescription>
                      <FormMessage className="text-rose-500" />
                    </FormItem>
                  )}
                />

                <FormField
                  control={form.control}
                  name="livingRooms"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel className="text-slate-700 dark:text-slate-300">
                        <div className="flex items-center gap-2">
                          <Sofa className="h-4 w-4 text-slate-500 dark:text-slate-400" />
                          Number of Living Rooms
                        </div>
                      </FormLabel>
                      <FormControl>
                        <Input
                          type="number"
                          placeholder="1"
                          {...field}
                          className="bg-slate-50 dark:bg-slate-700/50 border-slate-200 dark:border-slate-600 focus:border-slate-400 dark:focus:border-slate-500"
                        />
                      </FormControl>
                      <FormDescription className="text-slate-500 dark:text-slate-400">
                        Total number of living rooms
                      </FormDescription>
                      <FormMessage className="text-rose-500" />
                    </FormItem>
                  )}
                />
              </div>
            </div>

            <CardFooter className="px-0 pt-6 pb-0 flex flex-col sm:flex-row gap-4">
              <Button
                type="button"
                variant="outline"
                className="w-full sm:w-auto border-slate-200 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-300"
                onClick={() => form.reset()}
              >
                Reset Form
              </Button>
              <Button
                type="submit"
                className="w-full sm:w-auto bg-emerald-600 hover:bg-emerald-700 text-white"
                disabled={isSubmitting}
              >
                {isSubmitting ? (
                  <>
                    <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                    Submitting...
                  </>
                ) : (
                  "Submit Property Details"
                )}
              </Button>
            </CardFooter>
          </form>
        </Form>
      </CardContent>
    </Card>
  )
}
